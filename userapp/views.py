from django.shortcuts import render,redirect
from django.contrib import messages
from userapp.models import UserModel, NewPass, UserFeedback
from django.core.mail import EmailMultiAlternatives
from FakeBusPass.settings import DEFAULT_FROM_EMAIL
from textblob import TextBlob
from datetime import datetime ,date
from dateutil.relativedelta import relativedelta
import random

# Create your views here.
def user_registration(request):
   
    if request.method == "POST" and  'profile' in request.FILES:
      
        name = request.POST.get("name")
        father_name = request.POST.get("fname")
        date_of_birth = request.POST.get("dob")
        gender = request.POST.get("male")
        email = request.POST.get("email")
        phone = request.POST.get("number")
        aadhar = request.POST.get("aadhar_no")
        profile = request.FILES["profile"]
        
        
        #GENERATE PASSWORD
        
        
        lower_case = "abcdefghijklmnopqrstuvwxyz"
        upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        Number = "0123456789"
        Symbol = "!@#$%^&*()_+-="
        
        use_for = lower_case + upper_case + Number + Symbol
        length_for_pass = 8
        
        password = "".join(random.sample(use_for,length_for_pass))
        print("Your password is generated")
       
        try:
            UserModel.objects.get(email = email)
            messages.info(request, "email already existed")
            return redirect('user_registration')
        except:
            UserModel.objects.create(
                name = name,
                father_name = father_name,
                date_of_birth = date_of_birth,
                gender = gender,
                email = email,
                phone = phone,
                aadhar_no = aadhar,
                profile = profile,
                password = password
            )
            mail = email
            html_content = f"<p>Dear User This is Your login credentials,</p> <p>Your Email ID : {email}</p> <p>Your Phone No. : {phone}</p> <p>Password : {password} </p><span><strong>" 
            from_mail = DEFAULT_FROM_EMAIL
            email = [mail]
            try:
                msg = EmailMultiAlternatives("Authentication Credentials", html_content, from_mail, email)
                msg.attach_alternative(html_content, "text/html")
                if msg.send():
                    print('sent')
                    messages.info(request, 'credentials has been sent successfully')
                    return redirect('user_login')
            except:
                messages.warning(request, "credentials could not be sent try again later")
                return redirect('user_registration')
            
            messages.success(request, "user register successfully")
            return redirect("user_login")
    
    return render(request, "user/main-user.html")

# USER_APPLYNewPass

def user_applynewpass(request):
    user_id = request.session['user_id']
    user = UserModel.objects.get(pk=user_id)
    alldetails = UserModel.objects.get(pk=user_id)
    apply_date = date.today()
    

    if request.method == "POST"  and  'buspassphoto' in request.FILES:
        
        name = request.POST.get("name")
        email = request.POST.get("email")
        aadhar = request.POST.get("aadhar")
        payment_mode = request.POST.get("payment")
        bus_travel_type = request.POST.get("buspassmode")
        mobile = request.POST.get("mobile")
        father = request.POST.get("father")
        date_of_birth = request.POST.get("dob")
        gender = request.POST.get("gender")
        pass_photo = request.FILES["buspassphoto"]
        passduration = int(request.POST.get("passduration"))
        city = request.POST.get("city")
        print(passduration,'ddddd')
        print(type(passduration))
        
        
        try:
            f=NewPass.objects.get(email=email)
            messages.info(request,"You have already applied for the pass")
            return redirect('user_applynewpass')
        except:
            if passduration == 1:
                result=apply_date + relativedelta(months=+1)
                print(result,'asdasdasd1')
           
            elif passduration == 2:
                result=apply_date + relativedelta(months=+2)
                print(result,'asdasdasd2')
            else:
                result = apply_date + relativedelta(months=+3)
                print(result,'asdasdasd3')
        NewPass.objects.create(name = name, 
                                    email = email , 
                                    aadhar =  aadhar , 
                                    payment_mode = payment_mode , 
                                    bus_travel_type = bus_travel_type , 
                                    mobile= mobile ,
                                    father = father , 
                                    date_of_birth = date_of_birth , 
                                    gender = gender, 
                                    pass_photo = pass_photo,
                                    alldetails = alldetails,
                                    pass_user = user,
                                    passduration = passduration,
                                    city = city,
                                    validity=result,
                                    )
        messages.success(request,"Apply sucessfully")
    return render(request, "user/user-applyNewPass.html",{'user':user})

# USER_DASHBOARD

def user_dashboard(request):
    user_id = request.session['user_id']
    user = UserModel.objects.get(pk=user_id)
    try:
        newpass = NewPass.objects.get(pass_user = user)
        c = UserModel.objects.all().count() 
        d = UserFeedback.objects.filter(feedback2=newpass).count()
        S = NewPass.objects.filter(pass_user =user).count()
        t = NewPass.objects.all().count()
        return render(request, "user/user-dashboard.html",{'c':c ,'d':d ,'s':S ,'t':t})
    except:
        newpass= None
        return render(request, "user/user-dashboard.html")
# USER_FEEDBACK

def user_feedback(request):
    user_id = request.session['user_id']
    user = UserModel.objects.get(pk=user_id)
    try:
        newpass = NewPass.objects.get(pass_user=user)
        if request.method =="POST":
            overall = request.POST.get('rating1')
            travelling = request.POST.get('rating2')
            suggestion = request.POST.get('commentText')
            analysis = TextBlob(suggestion)
            print(analysis.sentiment)
            print(overall,travelling ,suggestion)
            
            if not overall:
                messages.info(request,"Please give the overall ratings")
                return redirect(user_feedback)
            if not travelling:
                messages.info(request,"Please give the travelling ratings")
                return redirect(user_feedback)
            sentiment = ''
            if analysis.polarity >= 0.5:
                sentiment = 'VeryPositive'
            elif analysis.polarity > 0 and analysis.polarity < 0.5:
                sentiment = 'Positive'
            elif analysis.polarity < 0 and analysis.polarity >= -0.5:
                sentiment = 'Negative'
            elif analysis.polarity <= -0.5:
                sentiment = 'VeryNegative'
            else:
                sentiment = 'Neutral'
            UserFeedback.objects.create(overall=overall,travelling=travelling,suggestion=suggestion,feedback2=newpass,sentiment=sentiment)
            messages.success(request,"Feedback has been send successfully")
    except:
        newpass=None
    return render(request,"user/user-feedback.html",{'np':newpass})


# USER_LOGIN

def user_login(request):
     if request.method == "POST":
          
        emaill = request.POST.get("email")
        print(emaill)
        passwordd = request.POST.get("password")
        print(passwordd)

        try:
            user_details = UserModel.objects.get(email=emaill,password=passwordd)
            request.session['user_id'] = user_details.user_id
            print(user_details.user_id)
            
            messages.success(request,'login successfull')
            return redirect("user_dashboard")

        except:
            messages.error(request,'invalid email and password')
            return redirect("user_login")
              
     return render(request, "user/user-login.html")
 
 
 # USER_MYPASSDETAILS

def user_mypassdetails(request):
    id = request.session['user_id']
    user =  UserModel.objects.get(user_id=id)
    try:
       passdetails = NewPass.objects.get(pass_user=user)
    except:
        passdetails=None
    return render(request, "user/user-mypassdetails.html",{'data':passdetails})

# USER_MYPROFILE

def my_profile(request):
    id = request.session['user_id']
    user =  UserModel.objects.get(user_id=id)
    if request.method == "POST":
        # User_ID = request.POST.get('User_ID')
        Name = request.POST.get('Name')
        # Aadhar_No = request.POST.get('Aadhar_No')
        mobile_No = request.POST.get('mobile_No')
        Father_Name = request.POST.get('Father_Name')
        Email = request.POST.get('Email')
        Gender = request.POST.get('Gender')
        Date_Of_Birth = request.POST.get('dob')
        
        if not request.FILES.get('profile',False):
            user.name = Name
            user.phone = mobile_No 
            user.father_name = Father_Name
            user.email = Email 
            user.gender = Gender
            user.date_of_birth = Date_Of_Birth
            
        if request.FILES.get('profile',False):
            image = request.FILES['profile']
            user.name = Name
            user.phone = mobile_No 
            user.father_name = Father_Name
            user.email = Email 
            user.gender = Gender
            user.date_of_birth = Date_Of_Birth
            user.profile = image
        user.save()
        messages.success(request,"profile updated sucessfully")
        return redirect('user_myprofile')
    return render(request, "user/user-myprofile.html",{"user":user})

# USER_LOGOUT

def user_logout(request):
    messages.success(request, "user logout successfully")
    return redirect("main_home")



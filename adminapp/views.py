from django.shortcuts import render,redirect
from django.contrib import messages
from userapp.models import *
from django.contrib.auth import logout



# Create Your views here.
def admin_login(request):
    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("password")
        
        if name == "admin" and password == "admin":
            messages.success(request, "admin login successfully")
            return redirect("admin_dashboard")
        else:
            messages.error(request, "invalid admin name or password")
            return redirect("admin_login")

    return render(request, "admin/main-admin.html")

def admin_userfeedback(request):
    userfeedback = UserFeedback.objects.all()
    return render(request, "admin/admin-userfeedback.html",{'data':userfeedback})

def admin_sentimentanalysis(request):
    admin_sentimentanalysis = UserFeedback.objects.all()
    return render(request, "admin/admin-sentimentanalysis.html",{'data':admin_sentimentanalysis})

def admin_sentimentgraph(request):
    x=UserFeedback.objects.all()
    # y=UserFeedbackModel.objects.filter(text=text)
    verypositive= UserFeedback.objects.filter(sentiment="verypositive").count()
    verynegative= UserFeedback.objects.filter(sentiment="verynegative").count()
    positive= UserFeedback.objects.filter(sentiment="positive").count()
    negative= UserFeedback.objects.filter(sentiment="negative").count()
    neutral=UserFeedback.objects.filter(sentiment="neutral").count()
    return render(request, "admin/admin-sentimentgraph.html",{'vp':verypositive,'vn':verynegative,'p':positive,'ne':negative,'neutral':neutral})


def admin_pendingrequest(request):
    pending_request = NewPass.objects.filter(status = "pending")
    users = UserModel.objects.all()
    return render(request, "admin/admin-pendingrequest.html",{"users":pending_request})

def admin_dashboard(request):
    pq = NewPass.objects.all().count()
    ap = NewPass.objects.filter(status = 'accepted').count()
    rj = NewPass.objects.filter(status = 'rejected').count()
    to = NewPass.objects.all().count
    return render(request, "admin/admin-dashboard.html",{'pq':pq , 'ap':ap , 'rj':rj ,'to':to })

def admin_alldetails(request):
    alldetails = NewPass.objects.all()
    
    # data = NewPass.objects.get(alldetails=alldetails)
    return render(request, "admin/admin-alldetails.html",{'data':alldetails})

def admin_acceptreject(request,pass_id):
    data = NewPass.objects.get(pass_id=pass_id)
    return render(request, "admin/admin-acceptreject.html",{
        'data':data
    })


def accept_pass(request,pass_id):
    a=NewPass.objects.get(pass_id=pass_id)
    a.status = 'accepted'
    a.save(update_fields = ['status'])
    a.save()
  
    return redirect("admin_pendingrequest")


def reject_pass(request,pass_id):
    a=NewPass.objects.get(pass_id=pass_id)
    a.status = 'rejected'
    a.save(update_fields = ['status'])
    a.save()
  
    return redirect("admin_pendingrequest")
def admin_logout(request):
    logout(request)
    messages.success(request, "admin logout successfully")
    return redirect("admin_login")

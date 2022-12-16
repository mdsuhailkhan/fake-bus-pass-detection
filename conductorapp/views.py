from django.shortcuts import render,redirect
from django.contrib import messages

# Create Your views here.
def conductor_scanbuspass(request):
    return render(request, "conductor/conductor-scanbuspass.html")

def main_conductor(request):
    if request.method == "POST":
        name = request.POST.get("emailaddress")
        password = request.POST.get("password")
        
        if name == "conductor" and password == "conductor":
            messages.success(request,"conductor login successfully")
            return redirect("conductor_scanbuspass")
        else:
            messages.error(request, "invalid conductor name or password")
            return redirect("main_conductor")
    
    return render(request,"conductor/main-conductor.html")


def conductor_logout(request):
    messages.success(request, "conductor logout successfully")
    return redirect("main_conductor")

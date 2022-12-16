from django.shortcuts import render
from userapp.models import UserFeedback

# Create your views here.
def main_home(request):
    comment = UserFeedback.objects.all()[0:3]
    return render(request, "main/main-home.html",{'c':comment})


def main_contact(request):
    return render(request,"main/main-contact.html")


def main_about(request):
    return render(request,"main/main-about.html")
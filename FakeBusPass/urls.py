"""FakeBusPass URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mainapp import views as mainapp_views
from conductorapp import views as conductor_views
from userapp import views as user_views
from adminapp import views as admin_views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    #main
    path('admin/', admin.site.urls),
    path('',mainapp_views.main_home,name="main_home"),
    path('main_contact',mainapp_views.main_contact,name="main_contact"),
    path('main_about',mainapp_views.main_about,name="main_about"),
    
    
    #user
    path('user_registration',user_views.user_registration,name="user_registration"),
    path('user_applynewpass',user_views.user_applynewpass,name="user_applynewpass"),
    path('user_dashboard',user_views.user_dashboard,name="user_dashboard"),
    path('user_feedback',user_views.user_feedback,name="user_feedback"),
    path('user_login',user_views.user_login,name="user_login"),
    path('user_mypassdetails',user_views.user_mypassdetails,name="user_mypassdetails"),
    path('user_myprofile',user_views.my_profile,name="user_myprofile"),
    
    
     
    #admin
    path('admin_login',admin_views.admin_login,name="admin_login"),
    path('admin_userfeedback',admin_views.admin_userfeedback,name="admin_userfeedback"),
    path('admin_sentimentanalysis',admin_views.admin_sentimentanalysis,name="admin_sentimentanalysis"),
    path('admin_sentimentgraph',admin_views.admin_sentimentgraph,name="admin_sentimentgraph"),
    path('admin_pendingrequest',admin_views.admin_pendingrequest,name="admin_pendingrequest"),
    path('admin_dashboard',admin_views.admin_dashboard,name="admin_dashboard"),
    path('admin_alldetails',admin_views.admin_alldetails,name="admin_alldetails"),
    path('admin_acceptreject/<int:pass_id>',admin_views.admin_acceptreject,name="admin_acceptreject"),
    path('accept_pass/<int:pass_id>',admin_views.accept_pass,name="accept_pass"),
    path('reject_pass/<int:pass_id>',admin_views.reject_pass,name="reject_pass"),

    path('admin-logout/',admin_views.admin_logout,name="admin_logout"),
     
    
    
    #conductor
    path('conductor_scanbuspass',conductor_views.conductor_scanbuspass,name="conductor_scanbuspass"),
    path('main_conductor',conductor_views.main_conductor,name="main_conductor"),
    path('conductor-logout/',conductor_views.conductor_logout,name="conductor_logout")
    
    
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   


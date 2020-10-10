"""Resume_create URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.shortcuts import render
from resume.views import resumeCreate,Register,logoutpage,resumedetails,resumeview,index,resumeEdit,resumeDelete
urlpatterns = [
    path('index', index, name='index'),
    path('resumeCreate',resumeCreate,name='createresume'),
    path('Register',Register,name='Register'),
    path('logoutpage',logoutpage,name='logoutpage'),
    path('resumeview/<int:pk>',resumeview,name='resumeview'),
    path('resumedetails',resumedetails, name='resumedetails'),
    path("",lambda request:render(request,"resume/base.html")),
    path('resumeEdit/<int:pk>', resumeEdit, name='resumeEdit'),
    path('resumeDelete/<int:pk>',resumeDelete, name='resumeDelete'),
]

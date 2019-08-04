"""Myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from Myproject.apps.home import views
from django.contrib import admin

urlpatterns = [
    url(r'nav/head/', views.Nav.as_view()),
    url(r'benner/', views.Benner.as_view()),
    url(r'nav/area/', views.Area.as_view()),
    url(r'nav/bottom/', views.Nav_Bottom.as_view()),
    url(r"nav/xiaoqu/",views.Housing_estate.as_view()),
    url(r"room_type/",views.Room_type.as_view()),
    url(r"area_houre/",views.Area_houre.as_view()),
    url(r"area_houre/",views.Area_houre.as_view()),
    # url(r"jrtj_list",views.Jrtj_list.as_view()),
    #下列为精品房 #四种筛选条件
    url(r"jpfy/",views.JPFY.as_view()),
    url(r"Today_preferential/",views.Today_preferential.as_view()),


]

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login , name='login'),
    path('register', views.register, name='register'),
    path('registeruser', views.registeruser, name='regiteruser'),
    path('loguser', views.loguser, name='loguser'),
    path('logout', views.logout, name='logout'),
    path('shippingdata', views.shippingaddress, name='shippingdata'),
    path("deleteaddress/<str:pid>", views.deleteaddress, name="deleteaddress"),
    path("deleteuser/<str:pid>", views.deleteuser, name="deleteaddress"),
]
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage , name='homepage'),
    path('item/<str:pid>', views.itempage, name='itempage'),
    path('category/<str:category>', views.productpage, name='productpage'),
    path('mycart', views.cartpage, name='mycart'),
    path("addtocart", views.addtocart, name="addtocart"),
    path("shippingpage", views.shippingpage, name="shippingpage"),
    path("placeorder", views.placeorder, name="placeorder"),
    path("deletecartitem/<str:pid>", views.deletecartitem, name="deletecartitem"),
    path("searchitem", views.searchitem, name="searchitem"),    
    path("userprofile", views.userprofile, name="userprofile"),    
    
]

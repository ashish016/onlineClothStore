
from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    #path('',views.index),
    path('',views.index,name="home_page"),
    path('login',views.login ,name="login_page" ),
    #path('login_action',views. ,name="login_action"),
    path('signin',views.signin,name="login_action" ),
    path('register',views.register, name="register" ),
    path('signup',views.signup,name="signup_action"),
    path('add_Products',views.add_Products,name="add_Products"),
    path('add_Product',views.add_Product,name="add_Product"),
    path('view_My_Products',views.view_My_Products,name='view_My_Products'),
    path('ajaxdata',views.ajaxdata,name='ajaxdata'),
    path('editajaxdata',views.editajaxdata,name='editajaxdata'),
    path('logout',views.logout,name='logout')


]

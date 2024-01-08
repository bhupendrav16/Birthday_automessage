
from django.contrib import admin
from django.urls import path,include
from .views import home,contact,navbar,info,birthday_day,messagepage

urlpatterns = [
    path("home/",home,name="home" ),
    path("contact/",contact,name="contact" ),
    path("info/",info, name = "info"),
    path("birthday_day",birthday_day, name = "birthday_day"),
    path("messagepage/",messagepage,name= "messagepage"),
    path("",navbar,name ="navbar"),    
]

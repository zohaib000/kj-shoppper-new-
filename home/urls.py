from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
      path("",views.home.as_view(),name="home"),
  ]

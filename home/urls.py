from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
  path("",views.story,name="story"),
  path("story_submit",views.story_submit,name="story_submit"),
  path("post",views.post,name="post"),
  path("post_submit",views.post_submit,name="post_submit"),
  path("profile",views.profile,name="profile"),
  path("profile_submit",views.profile_submit,name="profile_submit"),

]

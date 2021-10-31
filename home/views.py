
from django.shortcuts import render,HttpResponse
import requests
import urllib.request
import re 
import glob
import random
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import os
from instaloader import Post
from instaloader import Profile
import instaloader
from urllib.request import urlopen
from pc.settings import MEDIA_ROOT
from zipfile import ZipFile

def story(request):
    return render(request, "home/story.html")

def story_submit(request):
    if request.method == "POST":
        fa = request.POST.get("fa")
        if fa.startswith(" "):
            fa = fa[1:]
        directory = "instagram stories"
        parent_dir = "static"
        path = os.path.join(parent_dir, directory)
        name = fa
        f = os.path.join(path, name)
       
        try:
            os.makedirs(path)
            os.makedirs(f)
            instance = instaloader.Instaloader(dirname_pattern=f,download_pictures=False, download_videos=True, download_video_thumbnails=False, download_geotags=False, download_comments=False, save_metadata=False, compress_json=False, post_metadata_txt_pattern=" ", storyitem_metadata_txt_pattern=" ")
            try:
              instance.login('free_unlimited_tools', 'Daniyal1122')
            except:
              return render(request,'home/story.html',{'a':'Instagram Login error! please check your Username and Password OR Try again after sometime'})
            profile = Profile.from_username(
                instance.context, username=name)
            instance.download_stories(
                userids=[profile.userid], filename_target='story'.format(profile.username))
        except:
            try:
                os.makedirs(f)
                instance = instaloader.Instaloader(dirname_pattern=f,download_pictures=False, download_videos=True, download_video_thumbnails=False, download_geotags=False, download_comments=False, save_metadata=False, compress_json=False, post_metadata_txt_pattern=" ", storyitem_metadata_txt_pattern=" ")
                try:
                   instance.login('free_unlimited_tools', 'Daniyal1122')

                except:
                   return render(request,'home/story.html',{'a':'Instagram Login error! please check your Username and Password OR Try again after sometime'})
                profile = Profile.from_username(
                    instance.context, username=name)
                instance.download_stories(
                    userids=[profile.userid], filename_target='story'.format(profile.username))
            except:
                instance = instaloader.Instaloader(dirname_pattern=f,download_pictures=False, download_videos=True, download_video_thumbnails=False, download_geotags=False, download_comments=False, save_metadata=False, compress_json=False, post_metadata_txt_pattern=" ", storyitem_metadata_txt_pattern=" ")
                try:
                  instance.login('free_unlimited_tools', 'Daniyal1122')

                except:
                  return render(request,'home/story.html',{'a':'Instagram Login error! please check your Username and Password OR Try again after sometime'})

                profile = Profile.from_username(
                    instance.context, username=name)
                instance.download_stories(
                    userids=[profile.userid], filename_target='story'.format(profile.username))
        Q=glob.glob("static/instagram stories/"+fa+"/*")
        zipObj = ZipFile("static/"+fa+'.zip', 'w')
        for i in Q:
            sub=i[25:len(i)+1]
            zipObj.write(i,sub)
        name="static/"+fa+".zip"

        videos=[]
        pics=[]
        for i in Q:
            if i.endswith('.mp4'):
                videos.append(i)
            elif i.endswith('.jpg'):
                pics.append(i)
            else:
                a=5
        return render(request, "home/story.html", {'videos':videos,'pics':pics,"a":str(len(Q))+" stories found.CLick on below button to download.","b":name,"account":fa,"display":"visible"})
    else:
        return render(request,'home/story.html')
    return render(request,'home/story.html')



def post(request):
    return render(request, "home/post.html")


def post_submit(request):
    directory_path="static"
    if request.method == "POST":
        # https://www.instagram.com/p/CSsAUVRBfFT/?utm_source=ig_web_copy_link
        url = request.POST.get("url")
        if url.startswith(" "):
            url = url[1:]
        m = random.randint(0, 1000)
        f =str(m)
        p = os.path.join(directory_path,f)
        os.makedirs(p)
        short_url = url[28:len(url)-29]
        i = instaloader.Instaloader(dirname_pattern=p, sleep=True, quiet=False, user_agent=None, filename_pattern=None, download_pictures=True, download_videos=True, download_video_thumbnails=True, download_geotags=False, download_comments=False, save_metadata=True, compress_json=True,
                                    post_metadata_txt_pattern=None, storyitem_metadata_txt_pattern=None, max_connection_attempts=3, request_timeout=300.0, rate_controller=None, resume_prefix='iterator', check_resume_bbd=True, slide=None, fatal_status_codes=None, iphone_support=True, title_pattern=None)
        u1 = "free_unlimited_tools"
        p1 = "Daniyal1122"
        try:
          i.login(u1,p1)
        except:
          return render(request,'home/post.html',{'a':'Instagram Login Error! check your username and password . OR Try Again After sometime.'})
        try:
          post = Post.from_shortcode(i.context, short_url)
          i.download_post(post, target=f)
        except:
          return render(request,'home/post.html',{'a':'Please Enter correct Link of Post.'})
        Q=glob.glob("static/"+f+"/*")
        zipObj = ZipFile("static/post.zip", 'w')
        count=0
        for i in Q:
            sub=i[9+len(f):len(i)+1]
            if sub.endswith(".txt") or sub.endswith(".xz"):
                print("bad")
            else:
                zipObj.write(i,sub)
                count=count+1
        name="static/post.zip"
        videos=[]
        pics=[]
        for i in Q:
            if i.endswith('.mp4'):
                videos.append(i)
            elif i.endswith('.jpg'):
                pics.append(i)
            else:
                b=4
        print(Q)
        des=str(count)+" posts are found.Click on below button to download."
        return render(request, "home/post.html", {"a":des,"b":name,"display":"visible",'pics':pics,'videos':videos})
    return render(request, "home/post.html", {"a": "please enter link correctly."})

def profile(request):
    return render(request, "home/profile.html")


def profile_submit(request):
    directory_path="static"
    if request.method == "POST":
        name = request.POST.get("name")
        if name.startswith(" "):
            name = name[1:]
        r=random.randint(0,1000)
        name2=name+str(r)
        path = os.path.join(directory_path, name2)
        os.makedirs(path)
        mod = instaloader.Instaloader(dirname_pattern=path)
        try:
           mod.login("free_unlimited_tools","Daniyal1122")
           mod.download_profile(name, profile_pic_only=True)
        except:
           return render(request,'home/profile.html',{'a':"Invalid username or Login error! Please Try again after sometime !"})
        Q=glob.glob("static/"+name2+"/*")
        l=[]
        for i in Q:
            if i.endswith(".jpg") or i.endswith(".png") or i.endswith("jpeg"):
                l.append(i)
        return render(request, "home/profile.html", {"a": "Profile picture is Found.Click on below button to donwload.","b":l,"display":"visible"})

    


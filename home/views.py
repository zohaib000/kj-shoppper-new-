from django.http.response import HttpResponseRedirect
from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.views import View
import requests

class home(View):
    def get(self,request):
        city=request.GET.get('city')
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=ebdec6e0cdd6b6863b31dcc52a67ef9e"
        json=requests.get(url).json()
        
        context={
        "city_name":json['name'],
        "country":json['sys']['country'],
        "wind_speed":json['wind']['speed'],
        "temp":"{:.2f}".format(round(json['main']['temp']-273, 2)),
        "pressure":json['main']['pressure'],
        "humidity":json['main']['humidity'],
        "description":json['weather'][0]['description'],
        "icon":json['weather'][0]['icon'],
        }
        print(context)
        return render(request,'home/home.html',context)
    

        
        

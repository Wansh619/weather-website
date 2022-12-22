from django.shortcuts import render,redirect
import json
import requests

from django.contrib import messages
# Create your views here.
def index(request):
            
    return render(request,'index.html')

def pred(request):
    if request.method =='POST':
                city= request.POST['city']
                url = "https://yahoo-weather5.p.rapidapi.com/weather"
                querystring = {"location":city,"format":"json","u":"f"}
                 
                headers = {
	            "X-RapidAPI-Key": "7ded08e7b9msh384ca87b17abdbdp1cea7fjsne2dca62acd48",
	            "X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com"
                }
                response = requests.request("GET", url, headers=headers, params=querystring)
                print(response.json())
                
                data =response.json()
                if data is None:
                    messages.info(request,"CITY NOT FOUND")
                weather={
                    'country':data['location']['country'],
                    
                    "City":data['location']['city'],
                    'humidity':data['current_observation']['atmosphere']['humidity'],
                    'Temprature':data['current_observation']['condition']['temperature'],

                }
                return render(request,'index.html',weather)
    return redirect('index')
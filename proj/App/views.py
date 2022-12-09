from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from App.models import Obj
#from django.middleware.csrf import get_token
#from django.contrib.auth import authenticate, login
# Create your views here.

#@csrf_exempt
def recieve(request):
    #when we recieve a Post request
    if request.method == 'POST':
        if request.POST.get('micro') and request.POST.get('capteur') and request.POST.get('valeur'):
            obj=Obj()       #create an instence from our model
            obj.nameMicro= request.POST.get('micro')        #put the recieved data with the right attribute
            obj.nameCapteur= request.POST.get('capteur')
            obj.donnee = request.POST.get('valeur')
            obj.save()          #save it as an obj in the dataBase
            return HttpResponse('<h1>Data saved</h1>')
        
    #when we recieve a Get request
    if request.method == 'GET':
        return render(request,'hello.html')



from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from App.models import Obj

from rest_framework import viewsets
from rest_framework import permissions
from App.serializers import objSerializer


def recieve(request):
    #when we recieve a Post request
    print("Request recieved...\n")
    if request.method == 'POST':
        if request.POST.get('micro') and request.POST.get('capteur') and request.POST.get('valeur'):
            obj=Obj()                                       #create an instence from our model
            obj.nameMicro= request.POST.get('micro')        #put the recieved data with the right attribute
            obj.nameCapteur= request.POST.get('capteur')
            obj.donnee = request.POST.get('valeur')
            obj.save()                                      #save it as an obj in the dataBase
            return HttpResponse('<h1>Data saved</h1>')
        
    #when we recieve a Get request
    if request.method == 'GET':
        return render(request,'hello.html')

#retourne tous les informations de la base de donnees et afficher l aide de "objSerializer"
class objViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows object data to be viewed or edited.
    """
    queryset = Obj.objects.all()
    serializer_class = objSerializer
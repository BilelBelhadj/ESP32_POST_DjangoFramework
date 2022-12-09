from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from App.models import Obj
#from django.middleware.csrf import get_token
#from django.contrib.auth import authenticate, login
# Create your views here.

#@csrf_exempt
def recieve(request):
    if request.method == 'GET':
        return render(request,'hello.html')



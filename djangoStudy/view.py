from django.http import HttpResponse
from django.template.context_processors import request
from django.shortcuts import render

from djangoStudy.modules import *
from . modules import FamilyUser

def hello(request):
    return HttpResponse("Hello World!");

def hello2(request):
    return HttpResponse("Hello world2 ! ")

def hello3(request):
    context = {}
    context['hello'] = 'Hello Cory!'
    return render(request, 'index.html', context)

def arysDemo(request):
    data = [1,2,3,4,5,6,7]
    return render(request, 'listdemo.html', {'data':data}) #这里传的是字典，字典的键一定要和html页面中的一致

def familys(request):
    reqGender = request.GET["gender"]
    users = FamilyUser.objects.filter(gender=reqGender)
    return render(request, 'familys.html', {'users': users})

from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
# Create your views here.

def home(request):
    welcome = 'Welcome to my image Gallery'
    return render (request,'home.html',{'message': welcome})

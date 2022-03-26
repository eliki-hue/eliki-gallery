from tkinter import Image
from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
# Create your views here.

def home(request):
    welcome = 'Welcome to my image Gallery'
    images= Image.objects.get()
    return render (request,'home.html',{'message': welcome})

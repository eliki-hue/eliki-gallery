
from django.shortcuts import render,redirect
from datetime import datetime as dt
from django.http import HttpResponse, Http404

from myGallery.models import Image
# Create your views here.

def home(request):
    welcome = 'Welcome to my image Gallery'
    
    # date = dt.date.today()
    # news = Image.todays_news()
    images=Image.objects.all()
    return render (request,'home.html',{'message': welcome, 'images':images})

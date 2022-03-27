
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

def search_results(request):

    if 'image_category' in request.GET and request.GET["image_category"]:
        search_term = request.GET.get("image_category")
        searched_category = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_category})

    elif 'image_id' in request.GET and request.GET["image_id"]:
        search_term = request.GET.get("image_id")
        searched_category = Image.get_image_by_id(search_term)
        message = f"{search_term}"

        return render(request, 'search_id.html',{'message':message,"image_id": searched_category})

    elif 'image_location' in request.GET and request.GET["image_location"]:
        search_term = request.GET.get("image_location")
        searched_category = Image.filter_by_location(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_category})



    else:
        message = "You haven't searched for any category"
        return render(request, 'search.html',{"message":message})


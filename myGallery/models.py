from tkinter import image_names
from django.db import models
from datetime import datetime as dt

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length =60)
    image_description= models.TextField()
    image_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    image_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
   

    
    # @classmethod
    # def todays_news(cls):
    #     today = dt.date.today()
    #     images = cls.objects.filter(post = today)
    #     return images

    @classmethod
    def location_images(cls,place):
        images = cls.objects.filter(post_date = place)
        return images

    @classmethod
    def search_by_title(cls,search_term):
        images = cls.objects.filter(title__icontains=search_term)
        return images

class Location(models.Model):
    location = models.CharField(max_length=30)
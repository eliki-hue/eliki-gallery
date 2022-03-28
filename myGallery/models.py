
from tkinter import image_names
from unicodedata import category
from django.db import models
from datetime import datetime as dt


# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=30)

    
        
    
    def __str__(self):
        return self.location

    def save_location(self):
        self.save()

    def delete_location(self,place):
        to_delete= Location.objects.filter(location=place).delete()
    
    def update_location(self,location,new_location):
        Location.objects.filter(location=location).update(location=new_location)
        self.save()
        
   
        



class Category(models.Model):
    name = models.CharField(max_length =30)
   
    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self,category):
        to_delete= Category.objects.filter(name=category).delete()
    
    def update_category(self,category,new_category):
        Category.objects.filter(name=category).update(name=new_category)
        self.save()





class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length =60)
    image_description= models.CharField(max_length=100)
    image_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    image_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
   
    
    
    def __str__(self):
        return self.image_name


    def save_image(self):
        self.save()

    @classmethod
    def search_by_category(cls,category):
        items = cls.objects.filter(image_category_icontains=category)
        return items

    @classmethod
    def get_image_by_id(cls,id):
        items = cls.objects.get(id=id)
        return items

    @classmethod
    def filter_by_location(cls,location):
        items = cls.objects.filter(image_location_icontains=location)
        return items


    # @classmethod
    # def todays_news(cls):
    #     today = dt.date.today()
    #     images = cls.objects.filter(post = today)
    #     return images


    # @classmethod
    # def location_images(cls,place):
    #     images = cls.objects.filter(image_location = place)
    #     return images

    # @classmethod
    # def search_by_title(cls,search_term):
    #     images = cls.objects.filter(title__icontains=search_term)
    #     return images

    # @classmethod
    # def days_news(cls,date):
    #     news = cls.objects.filter(post_date__date = date)
    #     return news


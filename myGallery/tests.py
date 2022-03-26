from email.mime import image
from tkinter import image_names
from django.test import TestCase

# from myGallery.models import Image
from models import Location, Category, Image
# Create your tests here.

class ImageTestClass(TestCase):

    def setUp(self):
        
        self.new_location= Location(name = 'test_location')
        self.new_location.save()

        self.new_category= Category(name = 'test_category')
        self.new_category.save()


        self.image1=Image(image='image1.png',image_name="image1",image_description='test image', image_lacation="test_location",image_category="test_category")

        self.image1.save()

    #  # Creating a new tag and saving it
    #     self.new_location= Location(name = 'test_location')
    #     self.new_location.save()

    #     self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.james)
    #     self.new_article.save()

    #     self.new_article.tags.add(self.new_tag)

    # def tearDown(self):
    #     Editor.objects.all().delete()
    #     tags.objects.all().delete()
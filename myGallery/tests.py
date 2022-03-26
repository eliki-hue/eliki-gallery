from email.mime import image
from tkinter import image_names
from django.test import TestCase

# from myGallery.models import Image
from models import Location, Category, Image
# Create your tests here.

class ImageTestClass(TestCase):

    def setUp(self):
        self.image1=Image(image='image1.png',image_name="image1",image_description='test image',image_location='egerton',image_category='school')


    def test_save_image(self):
        self.image1.save_image()
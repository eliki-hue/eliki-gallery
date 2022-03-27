from django.test import TestCase

# from myGallery.models import Image
from .models import Location, Category, Image
# Create your tests here.

class LocationTestClass(TestCase):
    def setUp(self):
        self.new_location = Location(location ='test_location')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_location,Location))

    def test_save_method(self):
        self.new_location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)

    def test_delete_locations(self):       
        self.new_location.delete_location('test_location')           
        self.assertFalse(Location.objects.filter(location='test_location').exists())
            
    def test_updating(self):
        self.new_location.update_location(location='test_location',new_location='tes')
        self.assertTrue(Location.objects.filter(location='location2').exists())


#     def test_save_method(self):
#         self.new_category.save_category()
#         categories = Category.objects.all()
#         self.assertTrue(len(categories)>0)

# class ImageTestClass(TestCase):
    

#     def setUp(self):
        
#         self.test_location= Location(location = 'test_location')
#         self.test_location.save()

#         self.test_category= Category(name = 'test_category')
#         self.image_category.save()

#         self.image1=Image(image='image1.png',image_name="image1",image_description='test image', image_lacation="test_location",image_category="test_category")

#         self.image1.save_image()

#     def test_save_method(self):
#         self.image1.save_image()
#         images = Image.objects.all()
#         self.assertTrue(len(images) > 0) 

    #  # Creating a new tag and saving it
    #     self.new_location= Location(name = 'test_location')
    #     self.new_location.save()

    #     self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.james)
    #     self.new_article.save()

    #     self.new_article.tags.add(self.new_tag)

    # def tearDown(self):
    #     Editor.objects.all().delete()
        # tags.objects.all().delete()
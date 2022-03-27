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

    def test_updating(self):
        self.new_location.update_location(location='test_location',new_location='test_location2')
        self.assertFalse(Location.objects.filter(location='test_location2').exists())

    def test_delete_locations(self):       
        self.new_location.delete_location('test_location')           
        self.assertFalse(Location.objects.filter(location='test_location').exists())
            
   

   

class CategoryTestClass(TestCase):

    def setUp(self):
        self.new_category = Category(name ='test_category')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_category,Category))


    def test_save_method(self):
        self.new_category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)

    def test_updating(self):
        self.new_category.update_category(category='test_category',new_category='test_category2')
        self.assertFalse(Category.objects.filter(name='test_category2').exists())

    def test_delete_category(self):       
        self.new_category.delete_category('test_category')           
        self.assertFalse(Category.objects.filter(name='test_category').exists())

    

class ImageTestClass(TestCase):
    

    def setUp(self):
        
        self.test_location= Location(location = 'testlocation')
        self.test_location.save_location()

        self.test_category= Category(name = 'testcategory')
        self.test_category.save_category()

        self.image1=Image(image='image1.png',image_name="image1",image_description='test image', image_location="testlocation",image_category="testcategory")

        self.image1.save_image()

    def test_save_method(self):
        self.image1.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0) 

    

    # def tearDown(self):
    #     Editor.objects.all().delete()
        # tags.objects.all().delete()
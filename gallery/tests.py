from email.mime import image
from django.test import TestCase
# Django provides a test module django.test where we import the TestCase class.
#  We then import our models from the models module.
from .models import Location,Image,Category

# Create your tests here.
# Testing Image module

class ImageTestCase(TestCase):
    def setUp(self):
        self.image=Image(name='bear',image='',description='bear in Amazon' )

    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))
        
        self.category = Category(category='category')
        self.category.save()

        self.location = Location(location='location')
        self.location.save()

    def tearDown(self):
        Image.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()
    
    def test_get_imageby_id(self):
        image=Image.get_image_by_id()
        self.assertTrue(len(image)>0)

    def test_search_image(self):
        term='painting'
        results=Image.search_image(term)
        self.assertTrue(len(results)==0)

    def test_copy_image(self):
        image=Image.copy_image(id=1)
        self.assertTrue(len(image)==0)

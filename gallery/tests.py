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
        

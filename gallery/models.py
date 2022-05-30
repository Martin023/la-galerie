

from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class Location(models.Model):
    name= models.CharField(max_length=30)

    def __str__(self):
        return self.name

    
    def save_location(self):
        self.save()

    @classmethod
    def allLocations(cls):
        location=cls.objects.all()
        return location

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


    def save_category(self):
        self.save()

    @classmethod
    def allItems(cls):
        category=cls.objects.all()
        return category



class Image(models.Model):
    name= models.CharField(max_length=40)
    image=CloudinaryField('image')
    description=models.CharField(max_length=4000)
    date_added = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location,on_delete=models.DO_NOTHING )
    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING )

    def __str__(self):
        return self.name

     
    def save_image(self):
        self.save()

    @classmethod
    def display_image(cls):
        image=cls.objects.all()
        return image

    @classmethod
    def search_by_cat(cls,search_term):
        photo = cls.objects.filter(category__name__icontains=search_term)
        return photo










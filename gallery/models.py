
from email.mime import image
from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class Location(models.Model):
    name= models.CharField(max_length=30)

class Category(models.Model):
    name = models.CharField(max_length=30)


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
    def search_by_name(cls,search_term):
        photo = cls.objects.filter(title__icontains=search_term)
        return photo










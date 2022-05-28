from django.contrib import admin
from .models import Location,Image,Category

# Register your models here.
#Adding models to the admin page
admin.site.register(Location)
admin.site.register(Image)
admin.site.register(Category)

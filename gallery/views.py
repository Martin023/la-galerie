from django.shortcuts import render
import datetime as dt
from gallery.models import Image
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def home(request):
    images= Image.display_image()
    
    return render(request,'home.html',{"image":images} )

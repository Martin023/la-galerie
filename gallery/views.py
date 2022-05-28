from django.shortcuts import render

from gallery.models import Image

# Create your views here.

def home(request):
    images= Image.display_image()
    
    return render(request,'home.html',{"image":images} )

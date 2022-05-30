from django.shortcuts import render
import datetime as dt
from gallery.models import Category, Image, Location
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def home(request):
    images= Image.display_image()
    locations = Location.allLocations()
    
    return render(request,'home.html',{"image":images, "location":locations} )

def search_results(request):

    if 'art' in request.GET and request.GET["art"]:
        search_term = request.GET.get("art")
        searched_photos = Image.search_by_cat(search_term)
        message = f"{search_term}"

        return render(request, 'art/search.html',{"message":message,"photo": searched_photos})

    else:
        message = "You haven't searched for any term"
        return render(request, 'art/search.html',{"message":message})


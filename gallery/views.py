from django.shortcuts import render
import datetime as dt
from gallery.models import Image
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def home(request):
    images= Image.display_image()
    
    return render(request,'home.html',{"image":images} )

def search_results(request):

    if 'photo' in request.GET and request.GET["photo"]:
        search_term = request.GET.get("photo")
        searched_photos = Image.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"photo": searched_photos})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})



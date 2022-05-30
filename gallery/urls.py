
from . import views
from django.urls import re_path,path

urlpatterns = [
    re_path('home/', views.home,name='home-page'),
    path('search/',views.search_results,name='search_results'),
    
]

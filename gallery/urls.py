
from . import views
from django.urls import re_path

urlpatterns = [
    re_path('', views.home,name='home-page'),
    re_path('search/' ,views.search_results,name='search_results'),
    
]

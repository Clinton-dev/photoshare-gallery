from multiprocessing import context
from django.shortcuts import render
from .models import Category, Photo, Location

def get_category():
    categories = Category.objects.all()
    return categories

def get_location():
    location = Location.objects.all()
    return location

def home(request):
    context = {
        'locations': get_location,
        'categories': get_category
    }
    return render(request,'gallery/home.html', context)

def viewPhoto(request, pk):
    return render(request,'gallery/photo.html')

def createPhoto(request):
    return render(request,'gallery/create.html')
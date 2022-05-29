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
    photos = Photo.objects.all()
    context = {
        'locations': get_location,
        'categories': get_category,
        'photos': photos
    }
    return render(request,'gallery/home.html', context)

def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request,'gallery/photo.html', {'photo':photo})

def createPhoto(request):
    return render(request,'gallery/create.html')
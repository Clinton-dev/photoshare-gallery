from django.shortcuts import render, redirect
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
    context = {
        'categories': get_category,
        'locations': get_location
    }

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None

        if data['location'] != 'none':
            location = Location.objects.get(id=data['location'])
        elif data['location_new'] != '':
            location, created = Location.objects.get_or_create(name=data['location_new'])
        else:
            location = None

        photo = Photo.objects.create(
            category = category,
            location=location,
            description=data['description'],
            image=image
        )

        return redirect('home')

    return render(request,'gallery/create.html', context)
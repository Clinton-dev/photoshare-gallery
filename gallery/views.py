from django.shortcuts import render

def home(request):
    return render(request,'gallery/home.html')

def viewPhoto(request, pk):
    return render(request,'gallery/photo.html')

def createPhoto(request):
    return render(request,'gallery/create.html')
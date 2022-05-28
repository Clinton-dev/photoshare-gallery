from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('photo/<pk>/', views.viewPhoto,name='photo'),
    path('create/', views.createPhoto,name='create-photo'),
]
from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register-user'),
    path('', views.index),
    path('get-movies/', views.GetAllMovies),
    path('create-movie/', views.CreateMovie),
    path('delete-movie/', views.DeleteMovie),
    path('get-movie/', views.GetMovie),
    path('update-movie/', views.UpdateMovie),
    path('', include('movieApi.swagger')),
]
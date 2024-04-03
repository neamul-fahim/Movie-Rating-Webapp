from django.urls import path
from . import views

urlpatterns = [
    path('home-page/', views.HomePage.as_view(), name='homePage'),
    path('movies-API/', views.MovieListAPIView.as_view(), name='moviesAPI'),


]

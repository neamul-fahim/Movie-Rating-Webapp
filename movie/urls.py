from django.urls import path
from . import views

urlpatterns = [
    path('home-page/', views.HomePage.as_view(), name='homePage'),
    path('search-movie-page/', views.SearchMovieView.as_view(),
         name='searchMoviePage'),
    path('add-movie-page/', views.AddMovieView.as_view(),
         name='addMoviePage'),
    path('rate-movie-page/<int:movie_id>/<int:user_id>/',
         views.rate_movie.as_view(), name='rate_movie'),
    path('add-movie-API/', views.AddMovieAPIView.as_view(), name='addMovieAPI'),
    path('add-rating-API/', views.AddRatingAPIView.as_view(), name='addRatingAPI'),
    path('movies-API/', views.MovieListAPIView.as_view(), name='moviesAPI'),
    path('movie-API/<int:movie_id>/',
         views.MovieAPIView.as_view(), name='movieAPI'),

    path('search-movie-API/', views.SearchMoviesAPIView.as_view(),
         name='searchMovieAPI'),
]

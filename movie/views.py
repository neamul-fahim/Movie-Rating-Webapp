from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Movie
from .serializers import MovieModelSerializer


class HomePage(View):
    def get(self, request):
        template = "movie/home_page.html"
        context = {}
        return render(request, template, context)


class MovieListAPIView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieModelSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

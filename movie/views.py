from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, get_object_or_404
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Movie, Ratings
from .serializers import MovieModelSerializer, RatingsModelSerializer


class HomePage(View):
    def get(self, request):
        template = "movie/home_page.html"
        context = {}
        return render(request, template, context)


class SearchMovieView(View):
    def get(self, request):
        template = "movie/search_movie.html"
        context = {}
        return render(request, template, context)


class AddMovieView(View):
    def get(self, request):
        template = "movie/add_movie.html"
        context = {}
        return render(request, template, context)


class rate_movie(View):
    def get(self, request, movie_id, user_id):
        template = "movie/rating_movie.html"
        context = {'movie_id': movie_id,
                   'user_id': user_id,
                   }
        return render(request, template, context)


class AddMovieAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = MovieModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddRatingAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Fetching data
        data = request.data
        movie_id = data.get('movie')
        user_id = data.get('user')
        rating_value = data.get('rating')
        # Validate input data
        if not all([movie_id, user_id, rating_value]):
            return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Create a new rating
            rating = Ratings.objects.create(
                user_id=user_id,
                movie_id=movie_id,
                rating=rating_value
            )
            return Response({'success': 'Rating added successfully'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class MovieListAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieModelSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MovieAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, movie_id):
        movie = get_object_or_404(Movie, pk=movie_id)

        # Calculate average rating
        ratings = Ratings.objects.filter(movie=movie)
        total_rating = sum(rating.rating for rating in ratings)
        count = ratings.count()
        average_rating = total_rating / count if count > 0 else 0
        average_rating = round(average_rating, 2)

        # Construct JSON response
        movie_data = {
            'id': movie.id,
            'name': movie.name,
            'genre': movie.genre,
            'rating': movie.rating,
            'release_date': movie.release_date,
            'average_rating': average_rating
        }

        return Response(movie_data, status=status.HTTP_200_OK)


class SearchMoviesAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        movie_name = request.query_params.get('name', '')

        # Getting movies and Serializing
        movies = Movie.objects.filter(name__icontains=movie_name)
        movie_serializer = MovieModelSerializer(movies, many=True)

        # Getting all the movies average Rating
        movie_rating = {}
        for movie in movies:
            ratings = Ratings.objects.filter(movie=movie)
            ratings_serializer = RatingsModelSerializer(ratings, many=True)
            total_rating = 0
            count = 0
            for rating in ratings_serializer.data:
                total_rating += rating['rating']
                count += 1

            average_rating = total_rating / count if count > 0 else 0
            movie_rating[movie.id] = round(average_rating, 3)

        # Appending average rating to each movie
        for movie in movie_serializer.data:
            movie['average_rating'] = movie_rating.get(movie['id'], 0)

        return Response(movie_serializer.data, status=status.HTTP_200_OK)

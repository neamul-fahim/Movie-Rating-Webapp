from rest_framework import serializers
from .models import Movie, Ratings


class MovieModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class RatingsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = '__all__'

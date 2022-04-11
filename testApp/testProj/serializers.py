from .models import Login, People, Movies
from rest_framework import serializers

'''Serialize Model Objects'''

class GetLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ['user_id', 'name', 'email', 'phone', 'roles']

class PostLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ['name', 'password']

class PostMoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ['title', 'rating_classification', 'description', 'release_date']

class GetMoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'

class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ['person_id', 'name', 'location', 'description', 'died', 'roles']




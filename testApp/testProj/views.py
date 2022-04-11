from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Login, Movies, People
from .serializers import PostLoginSerializer, GetLoginSerializer, PostMoviesSerializer, GetMoviesSerializer, PeopleSerializer



@api_view(['GET', 'POST'])
def getLogin(request):
    '''user/login'''
    if request.method == 'POST':
        login = Login.objects.all()
        serialize = PostLoginSerializer(login, many=True)
        return JsonResponse(serialize.data)

    elif request.method == 'GET':
        get_login = Login.objects.all()
        serialize = GetLoginSerializer(get_login, many=True)
        return JsonResponse(serialize.data)

'''user/logout'''
@api_view(['GET'])
def logout(request):
    return Response("Created")

'''/movies 
   /movie:movie_id'''
@api_view(['GET', 'POST'])
def getMovies(request, id):
    if request.method == 'POST':
        movie = Movies.objects.all()
        serialize = PostMoviesSerializer(movie, many=True)
        return JsonResponse(serialize.data)

    elif request.method == 'GET':
        get_movie = Movies.objects.get(movie_id=id)
        serialize = GetMoviesSerializer(get_movie, many=False)
        return JsonResponse(serialize.data)

'''/people'''
@api_view(['GET'])
def getPeople(request):
    get_people = People.objects.all()
    serialize = PeopleSerializer(get_people, many=True)
    return JsonResponse(serialize.data)

'''/people/person_id'''
@api_view(['GET'])
def getPerson(request, id=0):
    get_people = People.objects.get(person_id=id)
    serialize = PeopleSerializer(get_people, many=False)
    return JsonResponse(serialize.data)



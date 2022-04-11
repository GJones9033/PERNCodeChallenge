from django.urls import path
from . import views

urlpatterns = [
    path('user/login', views.getLogin, name="login"),
    path('user/logout', views.logout, name="logout"),
    path('movies/<int:id>', views.getMovies, name="movies"),
    path('people', views.getPeople, name="people"),
    path('people/<int:id>', views.getPerson, name="person"),
]

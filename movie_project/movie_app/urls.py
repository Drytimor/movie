from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowAllMovies.as_view()),
    path('movie/<str:slug_movie>', views.ShowOneMovie.as_view(), name='details-movie'),
    path('directors/', views.ShowAllDirector.as_view()),
    path('directors/<int:id_director>', views.ShowOneDirector.as_view(), name='details-director'),
    path('actors/', views.ShowAllActor.as_view()),
    path('actors/<int:id_actor>', views.ShowOneActor.as_view(), name='details-actor'),
]
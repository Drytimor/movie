from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all_movie),
    path('movie/<str:slug_movie>', views.show_one_movie, name='details-movie'),
    path('directors/', views.show_all_director),
    path('directors/<int:id_director>', views.show_one_director, name='details-director'),
    path('actors/', views.show_all_actor),
    path('actors/<int:id_actor>', views.show_one_actor, name='details-actor'),
]
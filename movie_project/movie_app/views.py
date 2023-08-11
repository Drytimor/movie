from django.shortcuts import render, get_object_or_404
from .models import Movie, Director, Actor
from django.db.models import F, Max, Min, Sum, Avg, Count, Value
from django.views.generic import ListView
from django.views import View
from django.views.generic.base import TemplateView


class ShowAllMovies(ListView):

    model = Movie
    template_name = 'movie_app/html/all_movies.html'
    context_object_name = 'movies'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['agg'] = Movie.objects.aggregate(Avg('budget'), Min('rating'), Max('rating'), Count('id'))
        return context


class ShowOneMovie(TemplateView):
    template_name = 'movie_app/html/one_movies.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movie'] = Movie.objects.get(slug=kwargs['slug_movie'])
        return context

class ShowAllDirector(ListView):

    model = Director
    template_name = 'movie_app/html/all_director.html'
    context_object_name = 'director'

class ShowOneDirector(TemplateView):

    template_name = 'movie_app/html/one_director.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['director'] = Director.objects.get(id=kwargs['id_director'])
        return context

class ShowAllActor(ListView):

    model = Actor
    template_name = 'movie_app/html/all_actor.html'
    context_object_name = 'actor'

class ShowOneActor(TemplateView):

    template_name = 'movie_app/html/one_actor.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['actor'] = Actor.objects.get(id=kwargs['id_actor'])
        return context




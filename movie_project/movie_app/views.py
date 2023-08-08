from django.shortcuts import render, get_object_or_404
from .models import Movie, Director, Actor
from django.db.models import F, Max, Min, Sum, Avg, Count, Value




def show_all_movie(requests):
    movies = Movie.objects.order_by(F('rating').desc(nulls_last=True), 'year')
    agg = movies.aggregate(Avg('budget'), Min('rating'), Max('rating'), Count('id'))
    # for movie in movies:
    #     movie.save()
    return render(requests, 'movie_app/html/all_movies.html', {
        'movies': movies,
        'agg': agg
    })


def show_one_movie(requests, slug_movie):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(requests, 'movie_app/html/one_movies.html', {
        'movie': movie
    })


def show_all_director(requests):
    director = Director.objects.order_by('first_name', 'last_name')
    return render(requests, 'movie_app/html/all_director.html', {
        'director': director
    })

def show_one_director(requests, id_director):
    director = get_object_or_404(Director, id=id_director)
    return render(requests, 'movie_app/html/one_director.html', {
        'director': director
    })


def show_all_actor(requests):
    actor = Actor.objects.order_by('first_name', 'last_name')
    return render(requests, 'movie_app/html/all_actor.html', {
        'actor': actor
    })


def show_one_actor(requests, id_actor):
    actor = get_object_or_404(Actor, id=id_actor)
    return render(requests, 'movie_app/html/one_actor.html', {
        'actor': actor
    })


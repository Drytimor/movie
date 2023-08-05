from django.shortcuts import render, get_object_or_404
from .models import Movie
from django.db.models import F, Max, Min, Sum, Avg, Count, Value



def show_all_movie(requests):
    # movies = Movie.objects.order_by(F('year').desc(nulls_last=True))
    rating = 'rating'
    movies = Movie.objects.annotate(
        true_field=Value(True),
        false_field=Value(False),
        annot_field=F('rating') * F('year'),
    )
    agg = movies.aggregate(Avg('budget'), Min(rating), Max(rating), Count('id'))
    for movie in movies:
        movie.save()
    return render(requests, 'movie_app/html/all_movies.html', {
        'movies': movies,
        'agg': agg
    })


def show_one_movie(requests, slug_movie):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(requests, 'movie_app/html/one_movies.html', {
        'movie': movie
    })


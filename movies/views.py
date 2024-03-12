""" A file automatically created in each Django project. """

from django.http import Http404
from django.shortcuts import render

from .models import Movie



def index(request):
    newest_movies = Movie.objects.order_by('-release_date')[:15]
    context = {'newest_movies': newest_movies}
    return render(request, 'movies/index.html', context)
    
    
def show(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
    except Movie.DoesNotExist:
        raise Http404("Bear it in mind, you might want to check the name of the movie")
    return render(request, 'movies/show.html', {'movie': movie})


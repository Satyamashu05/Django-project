from django.shortcuts import render, get_object_or_404
from .models import Movie

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/movie_detail.html', {'movie': movie})

def home(request):
    movies = Movie.objects.all()  # Retrieve all movies from the database
    return render(request, 'movies/home.html', {'movies': movies})

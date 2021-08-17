from django.shortcuts import render
from django.views.generic import View
from .models import Movie

class MovieView(View):

    def get(self, request):
        movies = Movie.objects.all()
        return render(request, 'movies/movies.html', {'movies': movies})

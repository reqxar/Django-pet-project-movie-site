from django.db import models
from django.db.models.query import QuerySet
from django.db.models.query_utils import Q
from django.shortcuts import redirect, render
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Movie, Persons, Genre
from .forms import ReviewForm
from django.http import JsonResponse

class GenreYear:
    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Movie.objects.filter(draft=False).values('year')

class MovieView(GenreYear, ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = 'movies/movies.html'

class MovieDetailView(GenreYear, DetailView):
    model = Movie
    slug_field = 'url'

class AddReview(View):
    
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))
            form.movie = movie
            form.save()

        return redirect(movie.get_absolute_url())

class ActorView(GenreYear, DetailView):
    model = Persons
    template_name = 'movies/actor.html'
    slug_field = 'name'

class FilterMoviesView(GenreYear, ListView):
    template_name = 'movies/movies.html'
    def get_queryset(self):
        queryset = Movie.objects.filter(
            Q(year__in=self.request.GET.getlist('year')) |
            Q(genres__in=self.request.GET.getlist('genre'))
            )
        return queryset

class JsonFilterMoviesView(ListView):
    template_name = 'movies/movies.html'
    
    def get_queryset(self):
        queryset = Movie.objects.filter(
            Q(year__in=self.request.GET.getlist("year")) |
            Q(genres__in=self.request.GET.getlist("genre"))
        ).distinct().values("title", "tagline", "url", "poster")
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = list(self.get_queryset())
        return JsonResponse({"movies": queryset}, safe=False)

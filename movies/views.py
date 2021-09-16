from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Category, Movie
from .forms import ReviewForm

class MovieView(ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = 'movies/movies.html'

class MovieDetailView(DetailView):
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

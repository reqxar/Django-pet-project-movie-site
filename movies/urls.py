from django.urls import path
from .views import MovieView, MovieDetailView

urlpatterns = [
    path('', MovieView.as_view(), name='home'),
    path('<slug:slug>/', MovieDetailView.as_view(), name='movie_detail'),
]
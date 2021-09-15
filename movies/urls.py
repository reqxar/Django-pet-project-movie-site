from django.urls import path
from .views import AddReview, MovieView, MovieDetailView

urlpatterns = [
    path('', MovieView.as_view(), name='home'),
    path('<slug:slug>/', MovieDetailView.as_view(), name='movie_detail'),
    path('review/<int:pk>/', AddReview.as_view(), name='add_review'),
]
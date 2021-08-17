from django.contrib import admin
from .models import Category, Persons, Genre, Movie, MovieShoots, RatingStar, Rating, Reviews

admin.site.register(Category)
admin.site.register(Persons)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MovieShoots)
admin.site.register(RatingStar)
admin.site.register(Rating)
admin.site.register(Reviews)

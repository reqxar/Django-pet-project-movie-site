from modeltranslation.translator import register, TranslationOptions
from .models import Category, Persons, Movie, Genre, MovieShoots


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Persons)
class ActorTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Genre)
class GenreTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Movie)
class MovieTranslationOptions(TranslationOptions):
    fields = ('title', 'tagline', 'description', 'country')


@register(MovieShoots)
class MovieShotsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
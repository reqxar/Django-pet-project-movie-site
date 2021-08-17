from typing import Reversible
from django.db import models
from datetime import date
from django.urls import reverse

from django.db.models.base import Model

class Category(models.Model):
    name = models.CharField('Категория', max_length=150)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Persons(models.Model):
    name = models.CharField('Имя', max_length=120)
    age = models.PositiveSmallIntegerField('Возраст', default=0)
    description = models.TextField('Описание')   
    image = models.ImageField('Изображение', upload_to='persons/')     

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Актер / Режисер'
        verbose_name_plural = 'Актеры / Режисеры'

class Genre(models.Model):
    name = models.CharField('Жанр', max_length=150)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

class Movie(models.Model):
    title = models.CharField('Фильм', max_length=100)
    tagline = models.CharField('Слоган', max_length=100, default='')
    description = models.TextField('Описание')
    poster = models.ImageField('Постер', upload_to='movies/')
    year = models.PositiveSmallIntegerField('Год выпуска', default=2019)
    country = models.CharField('Страна', max_length=30)
    directors = models.ManyToManyField(Persons, verbose_name='Режиссер', related_name='film_director')
    actors = models.ManyToManyField(Persons, verbose_name='Актеры', related_name='film_actors')        
    genres = models.ManyToManyField(Genre, verbose_name='Жанры')
    world_premiere = models.DateField('Примьера в мире', default=date.today)
    budget = models.PositiveSmallIntegerField('Бюджет', default=0, help_text='Указать сумму в долларах')
    feels_in_usa = models.PositiveIntegerField('Сборы в США', default=0, help_text='Указать сумму в долларах')
    feels_in_world = models.PositiveIntegerField('Сборы в мире', default=0, help_text='Указать сумму в долларах')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField('Черновик', default=False)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={'slug': self.url})

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

class MovieShoots(models.Model):
    title = models.CharField('Заголовок', max_length=160)
    description = models.TextField('Описание')        
    image = models.ImageField('Изображение', upload_to='movie_shots/')
    movie = models.ForeignKey(Movie, verbose_name='Фильм', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Кадр из фильма'
        verbose_name_plural = 'Кадры из фильма'

class RatingStar(models.Model):
    value = models.PositiveSmallIntegerField('Значение', default=0)

    def __str__(self) -> str:
        return self.value

    class Meta:    
        verbose_name = 'Звезда рейтинга'
        verbose_name_plural = 'Звезды рейтинга'

class Rating(models.Model):
    ip = models.CharField('IP Адрес', max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE ,verbose_name='Звезда')    
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='Фильм')

    def __str__(self) -> str:
        return f'{self.star} - {self.movie}'

    class Meta:    
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'

class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField('Имя', max_length=160)
    text = models.TextField('Сообщение', max_length=5000)
    parent = models.ForeignKey('self', verbose_name='Родитель', on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, verbose_name='Фильм', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.name} - {self.movie}'

    class Meta:    
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'




    
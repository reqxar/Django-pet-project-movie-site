from django import forms
from django.db import models
from django.forms import fields
from .models import Reviews, Rating, RatingStar


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Reviews
        fields = ('name', 'email', 'text')

class RatingForm(forms.ModelForm):
    star = forms.ModelChoiceField(
        queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )

    class Meta:
        model = Rating
        fields = ('star',)
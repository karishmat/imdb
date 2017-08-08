__author__ = 'karishma'
from django import forms
from .models import Movies


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = '__all__'
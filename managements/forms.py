from django import forms
from .models import *

class AnimeForm(forms.ModelForm):
    class Meta:
        model = Anime
        exclude = ['imdb','click']
class SesonForm(forms.ModelForm):
    class Meta:
        model = Season
        fields = "__all__"
class EpisodeForm(forms.ModelForm):
    class Meta:
        model = Episode
        fields = "__all__"
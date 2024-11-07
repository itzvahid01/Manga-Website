from django.shortcuts import render
from managements.models import *

# Create your views here.
def index(request):
    lasted_animes = Anime.objects.all().order_by('-id')[:8]
    most_clicked_animes =Anime.objects.all().order_by('-click')[:8]
    most_imdb_animes = Anime.objects.all().order_by('-imdb')[:8]
    tags = TagList.objects.all()
    context = {"imdb_animes" : most_imdb_animes,"click_animes":most_clicked_animes,"lasted_animes" : lasted_animes,"tags": tags}
    return render(request,'user/home.html',context=context)
from django.shortcuts import render
from managements.models import *
from django.http import FileResponse
from main import settings
# Create your views here.
def index(request):
    lasted_animes = Anime.objects.all().order_by('-id')[:8]
    most_clicked_animes =Anime.objects.all().order_by('-click')[:8]
    most_imdb_animes = Anime.objects.all().order_by('-imdb')[:8]
    lasted_banner = Banner.objects.all().order_by('-pk')[:1]
    tags = TagList.objects.all()
    context = {"imdb_animes" : most_imdb_animes,"click_animes":most_clicked_animes,"lasted_animes" : lasted_animes,"tags": tags,"lasted_banner":lasted_banner[0]}
    return render(request,'user/home.html',context=context)
def anime_page(request,name):
    info = Anime.objects.get(title=name)
    seasons = Season.objects.filter(anime=info.pk)
    episode = Episode.objects.filter(anime=info.pk)
    context = {"anime" : info,"seasons":seasons,"episodes":episode}
    return render(request,"user/apage.html",context)

def download(request,anime_name,season_number,episode_number):
    anime = Anime.objects.get(title=anime_name)
    season = Season.objects.get(anime=anime.id,number=season_number)
    episode = Episode.objects.get(anime=anime.id,season=season,number=episode_number)
    return  FileResponse(open(f"{settings.BASE_DIR}\\media\\{episode.media.name}", 'rb'),filename=episode.media.name,as_attachment=True)
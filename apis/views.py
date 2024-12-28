from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import Response,status
import json
from main import settings
from django.http import FileResponse
from managements.models import *
from rest_framework import serializers

# Create your views here.
@api_view(['GET'])
def home(request):
    lasted_animes = Anime.objects.all().order_by('-id')[:8]
    lasted_banner = lasted_banner = Banner.objects.all().order_by('-pk')[:1][0]
    context = {}
    context['banner'] = {"title": f"{lasted_banner.anime}","img" :str(lasted_banner.img)}
    for item in lasted_animes:
        title = str(item.title)
        img = str(item.title_img)
        tags_class = TagList.objects.filter(anime_id=item.pk)
        tags = {}
        index = 1
        for tag_class in tags_class : 
            tags[f"Tag {index}"] =  f"{tag_class.tags}"
            index += 1
        anime = {"title" : title, "img" : img,"tags" : tags}
        context[item.title] = anime
    return Response(data=context,status=status.HTTP_202_ACCEPTED)

@api_view(["GET"])
def anime_page(request,name):
    anime = Anime.objects.get(title=name)
    seasons = Season.objects.filter(anime=anime.pk)
    episodes = Episode.objects.filter(anime=anime.pk)
    seasons_dict = {}
    episode_dict = {}
    for season in seasons:
        seasons_dict[f"Season {season.number}"] = episode_dict
        for episode in episodes:
            if episode.season.pk == season.pk:
                episode_dict[f"Episode {episode.number}"] = f"Season {episode.pk}"
    context = {
        "title" : str(anime.title),
        "banner" : str(anime.banner),
        "title_img" : str(anime.title_img),
        "description" : str(anime.description),
        "seasons" : str(seasons_dict)
    }
    return Response(data=context,status=status.HTTP_202_ACCEPTED)

@api_view(["GET"])
def get_episode(request,anime,season,episode):
    anime = Anime.objects.get(title=anime)
    season = Season.objects.get(number=season)
    episode = Episode.objects.get(anime=anime.pk,season=season,number=episode)
    context = {f"{anime.title} | {season.number} | {episode.number}" : str(episode.media)}
    return Response(data=context,status=status.HTTP_202_ACCEPTED)
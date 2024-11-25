from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import Response,status
import json
from main import settings
from django.http import FileResponse
from managements.models import *
from rest_framework import serializers

def get_image(address):
    with open(f"{settings.MEDIA_ROOT}\\{address}", 'r',encoding="utf8", errors='ignore') as f:
            return f.read()
# Create your views here.
@api_view(['GET'])
def home(request):
    lasted_animes = Anime.objects.all().order_by('-id')[:8]
    lasted_banner = lasted_banner = Banner.objects.all().order_by('-pk')[:1][0]
    context = {}
    context['banner'] = {"title": f"{lasted_banner.anime}","img" : get_image(lasted_banner.img)}
    for item in lasted_animes:
        title = item.title
        img = get_image(item.title_img)
        tags_class = TagList.objects.filter(anime_id=item.pk)
        tags = {}
        index = 1
        for tag_class in tags_class : 
            tags[f"Tag {index}"] =  f"{tag_class.tags}"
            index += 1
        anime = {"title" : title, "img" : img,"tags" : tags}
        context[item.title] = anime
    return Response(data=context,status=status.HTTP_202_ACCEPTED)
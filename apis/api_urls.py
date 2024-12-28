from django.urls import path
from .views import *

urlpatterns = [
    path('home/',home),
    path('anime/<str:name>',anime_page),
    path('anime/<str:anime>/<str:season>/<str:episode>',get_episode)
]
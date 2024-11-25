from django.urls import path
from .views import *

urlpatterns = [
   #------------------------ main ----------------------
    path("", index, name="home"),
    path("search/",index,name="search"), 
    path("about_us/",index,name="about_us"),
    #----------------------- film --------------------
    path("<str:name>/", anime_page, name="detail"),
    path("<str:anime_name>/<str:season_number>/<str:episode_number>/",download,name="download"),
    # ----------------------- profile ------------------------
    path("profile/", index, name="profile"),
]
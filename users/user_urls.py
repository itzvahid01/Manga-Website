from django.urls import path
from .views import *

urlpatterns = [
   #------------------------ main ----------------------
    path("", index, name="index"),
    path("search/",index,name="search"), 
    path("about_us/",index,name="about_us"),
    #----------------------- film --------------------
    path("<str:name>/", anime_page, name="detail"),
    path("<str:name>/<int:season>/<int:episode>", index, name="download"),
    # ----------------------- profile ------------------------
    path("profile/", index, name="profile"),
]
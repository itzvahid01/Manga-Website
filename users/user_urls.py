from django.urls import path
from .views import *

urlpatterns = [
    #------------------------     weblog -------------------
    path("weblog/",weblog_main,name="weblog_main"),
    path("weblog/<str:anime_name>/<str:title>/",weblog_page,name="weblog_page"),
    #----------------------- auth ----------------------
    path('login/',login_p,name="login"),
    path('register/',register_p),
   #------------------------ main ----------------------
    path("", index, name="home"),
    path("search/",index,name="search"), 
    path("about_us/",index,name="about_us"),
    #----------------------- film --------------------
    path("<str:name>/", anime_page, name="detail"),
    path("<str:anime_name>/<str:season_number>/<str:episode_number>/",download,name="download"),
    # ----------------------- profile ------------------------
    path("profile/", index, name="profile"),
    #------------------------     cats    ------------------------
    path("categury/<str:cat>/",cats_anime,name="cats_anime"),
]
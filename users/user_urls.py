from django.urls import path
from .views import *

urlpatterns = [
    #------------------------     weblog -------------------
    path("weblog/",weblog_main,name="weblog_main"),
    path("weblog/<str:anime_name>/<str:title>/",weblog_page,name="weblog_page"),
    #----------------------- auth ----------------------
    path('login/',login_p,name="login"),
    path('register/',register_p,name="register"),
    path('logout/',logout_view,name="logout"),
    path('verify_code/<str:phone_number>/',verify_phone,name="verify_phone"),
    # ----------------------- profile ------------------------
    path("profile/", profile, name="profile"),
    path("about_us/",about_us,name='about_us'),
   #------------------------ main ----------------------
    path("", index, name="home"),
    path("<str:name>/", index, name="sth"),
    #----------------------- film --------------------
    path("anime/<str:name>/", anime_page, name="detail"),
    path("anime/<str:anime_name>/<str:season_number>/<str:episode_number>/<str:languge>/",download,name="download"),
    #------------------------     cats    ------------------------
    path("categury/",cats_anime,name="categury"),
    path("categury/<str:cat>/",cats_anime,name="categury"),
]
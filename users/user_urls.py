from django.urls import path
from .views import index

urlpatterns = [
   #------------------------ main ----------------------
    path("", index, name="index"),
    path("search",index,name="search"), 
    path("about_us",index,name="about_us"),
    #----------------------- film --------------------
    path("<str:name>", index, name="detail"),
    path("<str:name>/<int:season>/<int:episode>", index, name="download"),
    # ----------------------- profile ------------------------
    path("profile/", index, name="profile"),
]
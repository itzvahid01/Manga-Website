from django.shortcuts import render,redirect
from managements.models import *
from django.http import FileResponse
from main import settings
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    lasted_animes = Anime.objects.all().order_by('-id')[:8:-1]
    most_clicked_animes =Anime.objects.all().order_by('-click')[:8:-1]
    most_imdb_animes = Anime.objects.all().order_by('-imdb')[:8:-1]
    lasted_banner = Banner.objects.all().order_by('-pk')[:1]
    tags = TagList.objects.all()
    context = {"imdb_animes" : most_imdb_animes,"click_animes":most_clicked_animes,"lasted_animes" : lasted_animes,"tags": tags,"lasted_banner":lasted_banner[0]}
    return render(request,'main/home.html',context=context)
def anime_page(request,name):
    info = Anime.objects.get(title=name)
    seasons = Season.objects.filter(anime=info.pk)
    episode = Episode.objects.filter(anime=info.pk).order_by('-number')[0::-1]
    posts = Post.objects.filter(anime=info.pk).order_by('-lmodified')[:4:-1]
    context = {"anime" : info,"seasons":seasons,"episodes":episode,"posts":posts}
    return render(request,"main/apage.html",context)

@login_required(login_url='login')
def download(request,anime_name,season_number,episode_number):
    anime = Anime.objects.get(title=anime_name)
    season = Season.objects.get(anime=anime.id,number=season_number)
    episode = Episode.objects.get(anime=anime.id,season=season,number=episode_number)
    return  FileResponse(open(f"{settings.BASE_DIR}\\media\\{episode.media.name}", 'rb'),filename=episode.media.name,as_attachment=True)
#------------------------------------------------ auth -----------------------------------------------
def login_p(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        return redirect('home')
    form = UserLoginForm()
    context = {'form' : form}
    return render(request,'auth/login.html',context)
def register_p(request): 
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form = UserRegisterForm(data=data)
            form.save()
            return redirect('home')
    form = UserRegisterForm()
    context = {'form' : form}

    return render(request,'auth/register.html',context)
#--------------------------------------- categury --------------------------------------
def cats_anime(request,cat):
    if cat == 'news':
        cat =  'id'
    elif cat == 'popular' :
        cat = 'click'
    elif cat == 'best':
        cat = 'imdb'
    animes = Anime.objects.all().order_by('-id')[:8:-1]
    tags = TagList.objects.all()
    context = {'animes' : animes,'tags' : tags}
    return render(request,'main/cpage.html',context)
#--------------------------------------- weblog --------------------------------------------
def weblog_main(request):
    posts = Post.objects.all()
    context = {'posts' : posts}
    return render(request,'blog/main.html',context)
def weblog_page(request,anime_name,title):
    anime = Anime.objects.get(title=anime_name)
    post = Post.objects.get(title=title)
    context = {'anime' : anime,'post' : post}
    return render(request,'blog/page.html',context)
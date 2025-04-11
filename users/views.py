from django.shortcuts import render,redirect,HttpResponse
from managements.models import *
from django.http import FileResponse
from main import settings
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from random import randint as r
from kavenegar import *
from hashlib import sha256

#------------------------- nigga -------------------------
def menu():
    menus = Menu.objects.all()
    menus_options = MenuOption.objects.all()
    return (menus,menus_options)
# Create your views here.
def index(request,name=None):
    lasted_animes = Anime.objects.all().order_by('-id')[:8:-1] or []
    most_clicked_animes =Anime.objects.all().order_by('-click')[:8:-1] or []
    most_imdb_animes = Anime.objects.all().order_by('-imdb')[:8:-1] or []
    lasted_banner = Banner.objects.first() or None
    tags = TagList.objects.all()
    menus, menus_options = menu()
    cat_shows = [
        {'title': 'جدید ها','address':'news','data':lasted_animes},
        {'title':'محبوب ها','address':'populer','data':most_clicked_animes},
        {'title':'بهترین ها','address':'best','data':most_imdb_animes}
        ]
    context = {"cat_shows":cat_shows,"menus":menus,"menus_options":menus_options,"imdb_animes" : most_imdb_animes,"click_animes":most_clicked_animes,"lasted_animes" : lasted_animes,"tags": tags,"lasted_banner":lasted_banner}
    return render(request,'main/home.html',context=context)
def about_us(request):
    menus, menus_options = menu()
    want_text_boxes = WantTextBox.objects.all()
    context = {"menus":menus,"menus_options":menus_options,'want_text_boxes':want_text_boxes}
    return render(request,'main/about_us.html',context=context)
def anime_page(request,name):
    info = Anime.objects.get(title=name)
    seasons = Season.objects.filter(anime=info.pk)
    episodes = Episode.objects.filter(anime=info.pk).order_by('-number')[0::-1] or []
    medias = Files.objects.filter(episode__anime=info.pk).order_by('-id') or []
    posts = Post.objects.filter(anime=info.pk).order_by('-lmodified')[:4:-1] or []
    menus, menus_options = menu()
    context = {"menus":menus,"menus_options":menus_options,"anime" : info,"seasons":seasons,"episodes":episodes,"posts":posts,'medias':medias}
    return render(request,"main/apage.html",context)

@login_required(login_url='login')
def download(request,anime_name,season_number,episode_number,languge):
    anime = Anime.objects.get(title=anime_name)
    season = Season.objects.get(anime=anime.id,number=season_number)
    episode = Episode.objects.get(anime=anime.id,season=season,number=episode_number)
    medias = Files.objects.filter(episode=episode.pk).first()
    if languge == "fa":
        media = medias.media_fa
    else:
        media = medias.media_en
    return  FileResponse(open(f"{settings.BASE_DIR}\\media\\{media}", 'rb'),filename=media.name,as_attachment=True)
#------------------------------------------------ auth -----------------------------------------------
def login_p(request):
    menus, menus_options = menu()
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        return redirect('home')
    form = UserLoginForm()
    context = {"menus":menus,"menus_options":menus_options,'form' : form}
    return render(request,'auth/login.html',context)
# views.py - register_p
def register_p(request):
    menus, menus_options = menu()
    form = UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            data_form = form.cleaned_data
            phone_number = data_form['phone_number']
            code = ''.join([str(r(0, 9)) for _ in range(6)])
            
            # ارسال پیامک
            api = KavenegarAPI('7479457562493361733437565141466258682F565752682B6D364C774D4B456A3248724B79456D683379733D')
            params = {
                'sender': '2000660110',
                'receptor': int(phone_number),
                'message': f'کد ورود لونیکا \n شماره موبایل : {phone_number} \n کد : {code}'
            }
            response = api.sms_send(params)

            # ذخیره اطلاعات در session
            request.session['verification_code'] = code
            request.session['phone_number'] = phone_number
            request.session['username'] = data_form['username']
            request.session['email'] = data_form['email']
            request.session['password'] = data_form['password']

            # هدایت به صفحه تأیید کد
            return redirect('verify_phone', phone_number=phone_number)
        else:
            errors = form.errors
    context = {"menus": menus, "menus_options": menus_options, 'form': form}
    return render(request, 'auth/register.html', context)
# views.py
# views.py - verify_phone
def verify_phone(request, phone_number):
    if request.method == "POST":
        entered_code = request.POST.get('code')
        stored_code = request.session.get('verification_code')
        stored_phone_number = request.session.get('phone_number')

        print("entered_code:", entered_code)
        print("stored_code:", stored_code)
        print("stored_phone_number:", stored_phone_number)
        print("phone_number:", phone_number)

        if entered_code == stored_code and stored_phone_number == phone_number:
            # ایجاد کاربر جدید
            user = CustomUser.objects.create_user(
                username=request.session.get('username'),
                email=request.session.get('email'),
                phone_number=stored_phone_number,
                password=request.session.get('password')
            )
            user.is_verified = True
            user.save()

            # لاگین کاربر
            login(request, user)

            # حذف اطلاعات از session
            del request.session['verification_code']
            del request.session['phone_number']
            del request.session['username']
            del request.session['email']
            del request.session['password']

            return redirect('home')
        else:
            return redirect('home')

    return render(request, 'auth/verify_phone.html')
@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('home')
#--------------------------------------- categury --------------------------------------
def cats_anime(request,cat):
    menus, menus_options = menu()
    animes = Anime.objects.all()
    tags_list = TagList.objects.all()
    tags = Tag.objects.all()
    ms = Menu.objects.filter(address=cat)
    animes_show = []
    #---------------------- Manga,Manha,Manhuwa,... -------------
    if request.GET.get('tag') == None:
        flag = False
        filter_word = None
    else :
        flag=True
        filter_word= request.GET.get('tag')
    if flag :
        for anime in animes :
            f1 = False
            f2= False
            for tag_list in tags_list :
                if anime.pk == tag_list.anime_id.pk :
                    for tag in tags :
                        if tag.pk == tag_list.tags.pk :
                            for m in ms :
                                if cat == f"{m.address}" :
                                    f1=True
                                if tag.title == filter_word :
                                    f2=True
            if f1:
                if f2:
                    animes_show.append(anime)
    else :
        for anime in animes :
            f1 = False
            for tag_list in tags_list :
                if anime.pk == tag_list.anime_id.pk :
                    for tag in tags :
                        if tag.pk == tag_list.tags.pk :
                            for m in ms :
                                if cat == f"{m.address}" :
                                    f1=True
            if f1:
                animes_show.append(anime)
        f3 = False
        if cat == 'news':
            cat =  'id'
            f3 = True
        elif cat == 'populer' :
            cat = 'click'
            f3 = True
        elif cat == 'best':
            cat = 'imdb'
            f3 = True
        if f3:
            animes_show = Anime.objects.all().order_by(f"{cat}")  
        else :
            for anime in animes :
                f1 = False
                for tag_list in tags_list :
                    if anime.pk == tag_list.anime_id.pk :
                        for tag in tags :
                            if tag.pk == tag_list.tags.pk :
                                for m in ms :
                                    if tag.title == f"{m}" :
                                        f1=True
                        if f1:
                            animes_show.append(anime)
    context = {"menus":menus,"menus_options":menus_options,'animes' : animes_show,'tags' : tags_list    }
    return render(request,'main/cpage.html',context)
#--------------------------------------- weblog --------------------------------------------
def weblog_main(request):
    posts = Post.objects.all()
    menus, menus_options = menu()
    context = {"menus":menus,"menus_options":menus_options,'posts' : posts}
    return render(request,'blog/main.html',context)
def weblog_page(request,anime_name,title):
    anime = Anime.objects.get(title=anime_name)
    post = Post.objects.get(title=title)
    menus, menus_options = menu()
    context = {"menus":menus,"menus_options":menus_options,'anime' : anime,'post' : post}
    return render(request,'blog/page.html',context)
#--------------------------------------- profile --------------------------------------------
@login_required(login_url='login')
def profile(request):
    menus, menus_options = menu()
    password = UserPasswordForm()
    username = UserNameForm()
    email = UserEmailForm()
    if request.user.is_staff:
        is_staff = True
    else:
        is_staff = False
    if request.method == "POST":
        return redirect('profile')
    else:
        context = {"menus":menus,"menus_options":menus_options,'email_form':email,'username_form':username,'password_form':password,'is_staff':is_staff}
        return render(request,'user/user.html',context)
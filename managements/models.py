from django.db import models as m
from django.conf import settings
from django.core.validators import MaxValueValidator,MinValueValidator
import os
def manga_upload_path_banner_titleimg(instance, filename):
    total_mangas = Anime.objects.count()
    folder_number = (total_mangas // 100) + 1

    # ساختار پوشه: animes/{folder_number}/{title}/{filename}
    return f"animes/{folder_number}/{instance.title}/{filename}"

# Create your models here.
class Anime(m.Model):
    title = m.CharField(max_length=255,unique=True)
    title_img = m.ImageField(null=True,blank=True,upload_to=manga_upload_path_banner_titleimg)
    description = m.TextField(null=True,blank=True)
    banner = m.ImageField(null=True,blank=True,upload_to=manga_upload_path_banner_titleimg)
    click = m.IntegerField(default=0,null=True,blank=True)
    folder_number = m.IntegerField(default=1)
    imdb = m.FloatField(default=0, help_text='value 0 to 10', validators=[MaxValueValidator(10),
        MinValueValidator(0)])
    created = m.DateField(auto_now_add=True,null=True,blank=True)
    lmodified = m.DateField(auto_now=True,null=True,blank=True)
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        total_mangas = Anime.objects.count()
        self.folder_number = (total_mangas // 100) + 1
        manga_dir = os.path.join(settings.MEDIA_ROOT, 'animes', str(self.folder_number), self.title)
        os.makedirs(manga_dir, exist_ok=True)
        super().save(*args, **kwargs)
class Tag(m.Model):
    title = m.CharField(max_length=255)
    created = m.DateField(auto_now_add=True,null=True,blank=True)
    lmodified = m.DateField(auto_now=True,null=True,blank=True)
    def __str__(self):
        return f"{self.title}"
class TagList(m.Model):
    anime_id = m.ForeignKey(Anime,on_delete=m.CASCADE,related_name="tags")
    tags = m.ForeignKey(Tag,on_delete=m.CASCADE)
    rating = m.IntegerField(default=0, help_text='value 1 to 100', validators=[MaxValueValidator(100),
            MinValueValidator(1)])
    created = m.DateField(auto_now_add=True,null=True,blank=True)
    lmodified = m.DateField(auto_now=True,null=True,blank=True)
    def __str__(self):
        return f"{self.anime_id.title} | {self.tags.title}"
class Season(m.Model):
    number = m.IntegerField(default=0,blank=True,null=True)
    anime = m.ForeignKey(Anime,on_delete=m.CASCADE,related_name="seasons",null=True,blank=True)
    created = m.DateField(auto_now_add=True,null=True,blank=True)
    lmodified = m.DateField(auto_now=True,null=True,blank=True)
    def __str__(self):
        return f"Season : {self.number} |{self.anime.title}"
    def save(self, *args, **kwargs):
        total_mangas = Anime.objects.count()
        self.anime.folder_number = (total_mangas // 100) + 1
        manga_dir = os.path.join(settings.MEDIA_ROOT, 'animes', str(self.anime.folder_number), str(self.anime.title),str(self.number))
        os.makedirs(manga_dir, exist_ok=True)
        super().save(*args, **kwargs)
class Episode(m.Model): 
    anime = m.ForeignKey(Anime,on_delete=m.CASCADE,related_name="episodes_a",null=True,blank=True)
    number = m.IntegerField(default=0,blank=True,null=True)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
    season = m.ForeignKey(Season,on_delete=m.CASCADE,related_name="episodes",null=True,blank=True)
    created = m.DateField(auto_now_add=True,null=True,blank=True)
    lmodified = m.DateField(auto_now=True,null=True,blank=True)
    def __str__(self):
        return f"Episode : {self.number} | {self.season} | {self.season.number }"
    def save(self, *args, **kwargs):
        total_mangas = Anime.objects.count()
        self.season.anime.folder_number = (total_mangas // 100) + 1
        manga_dir = os.path.join(settings.MEDIA_ROOT, 'animes', str(self.season.anime.folder_number), str(self.season.anime.title),str(self.season.number),str(self.number))
        os.makedirs(manga_dir, exist_ok=True)
        super().save(*args, **kwargs)
def manga_upload_path_files(instance, filename):
    return f"animes/{instance.episode.anime.folder_number}/{instance.episode.anime.title}/{instance.episode.season.number}/{instance.episode.number}/{filename}"
class Files(m.Model): 
    episode = m.ForeignKey(Episode,on_delete=m.CASCADE,related_name="media",null=True,blank=True)
    media_fa = m.FileField(null=True,blank=True,upload_to=manga_upload_path_files)
    media_en =  m.FileField(null=True,blank=True,upload_to=manga_upload_path_files)
    def save(self, *args, **kwargs):
        total_mangas = Anime.objects.count()
        self.episode.anime.folder_number = (total_mangas // 100) + 1
        super().save(*args, **kwargs)
class Product(m.Model):
    anime = m.ForeignKey(Anime,on_delete=m.CASCADE,related_name="product",null=True,blank=True)            

class Banner(m.Model):
    anime = m.ForeignKey(Anime,on_delete=m.CASCADE,related_name='ad',null=True,blank=True)
    img = m.ImageField(null=True,blank=True)
    created = m.DateField(auto_now_add=True,null=True,blank=True)
    lmodified = m.DateField(auto_now=True,null=True,blank=True)
    def __str__(self):
        return f"Anime | {self.anime}"
class Post(m.Model):
    anime = m.ForeignKey(Anime,on_delete=m.CASCADE)
    title = m.CharField(max_length=255,null=True,blank=True)
    title_img = m.ImageField(null=True,blank=True)
    text = m.TextField(null=True,blank=True)
    grade = m.FloatField(default=0, help_text='value 0 to 10', validators=[MaxValueValidator(10),
        MinValueValidator(0)])
    click = m.IntegerField(default=0,null=True,blank=True)
    created = m.DateField(auto_now_add=True,null=True,blank=True)
    lmodified = m.DateField(auto_now=True,null=True,blank=True)
    def __str__(self):
        return f"{self.anime} | {self.title}"

class Menu(m.Model):
    name_show = m.CharField(max_length=255,null=True,blank=True)
    address = m.CharField(max_length=255,null=True,blank=True)
    family=m.CharField(max_length=255,null=True,blank=True)
    def __str__(self):
        return f"{self.address}"
    
class MenuOption(m.Model):
    tag = m.ForeignKey(Tag,on_delete=m.CASCADE,null=True,blank=True)
    menu = m.ForeignKey(Menu,on_delete=m.CASCADE,related_name="menus",null=True,blank=True)
    title = m.CharField(max_length=255,null=True,blank=True)
    def __str__(self):
        return f"{self.menu}|  {self.title}"
class WantTextBox(m.Model):
    title = m.CharField(max_length=255,null=True,blank=True)
    text = m.TextField(null=True,blank=True)
    img = m.ImageField()
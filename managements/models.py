from django.db import models as m
from main import settings


# Create your models here.
class Anime(m.Model):
    title = m.CharField(max_length=255)
    title_img = m.ImageField(null=True,blank=True)
    description = m.TextField(null=True,blank=True)
    banner = m.ImageField(null=True,blank=True)
    click = m.IntegerField(default=0,null=True,blank=True)
    imdb = m.IntegerField(default=0,null=True,blank=True)
    def __str__(self):
        return self.title
    
class Tag(m.Model):
    title = m.CharField(max_length=255)
    def __str__(self):
        return f"{self.title}"
class TagList(m.Model):
    anime_id = m.ForeignKey(Anime,on_delete=m.CASCADE,related_name="tags")
    tags = m.ForeignKey(Tag,on_delete=m.CASCADE)
    def __str__(self):
        return f"{self.anime_id.title} | {self.tags.title}"
class Season(m.Model):
    number = m.IntegerField(default=0,blank=True,null=True)
    anime = m.ForeignKey(Anime,on_delete=m.CASCADE,related_name="seasons",null=True,blank=True)
    def __str__(self):
        return f"Season : {self.number} |{self.anime.title}"
class Episode(m.Model): 
    anime = m.ForeignKey(Anime,on_delete=m.CASCADE,related_name="episodes_a",null=True,blank=True)
    number = m.IntegerField(default=0,blank=True,null=True)
    season = m.ForeignKey(Season,on_delete=m.CASCADE,related_name="episodes",null=True,blank=True)
    media = m.FileField(null=True,blank=True)
    def __str__(self):
        return f"Episode : {self.number} | {self.season} | {self.season.number }"
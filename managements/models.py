from django.db import models as m


# Create your models here.
class Anime(m.Model):
    title = m.CharField(max_length=255)
    title_img = m.ImageField()
    description = m.TextField()
    banner = m.ImageField()
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
    anime = m.ForeignKey(Anime,on_delete=m.CASCADE,related_name="seasons",null=True,blank=True)
    def __str__(self):
        return f"Season : {self.pk} |{self.anime.title}"
class Episode(m.Model): 
    season = m.ForeignKey(Season,on_delete=m.CASCADE,related_name="episodes",null=True,blank=True)
    media = m.FileField(null=True,blank=True)
    def __str__(self):
        return f"Episode : {self.pk} | {self.season}"
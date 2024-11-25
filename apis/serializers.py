from rest_framework import serializers
from managements.models import *
class SAnime(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields= "__all__"

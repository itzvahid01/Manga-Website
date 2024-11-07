from django.shortcuts import render
from .forms import *

# Create your views here.
def admin_panel(request):
    context = {"anime_form":AnimeForm}
    return render(request,'admin.html',context)
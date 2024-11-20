from django.shortcuts import render
from .forms import *

# Create your views here.
def admin_panel(request):
    context = {"anime_form":AnimeForm}
    if request.method == 'POST':
        form = AnimeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form.save()
    return render(request,'admin.html',context)
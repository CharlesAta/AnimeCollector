from django.shortcuts import render
from .models import Anime
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def anime_index(request):
    anime = Anime.objects.all()
    return render(request, 'anime/index.html', { 'anime': anime })

def anime_detail(request, anime_id):
    anime = Anime.objects.get(id=anime_id)
    return render(request, 'anime/detail.html', { 'anime': anime })
from django.shortcuts import render
from .models import Anime
from django.views.generic.edit import CreateView, DeleteView, UpdateView

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

class AnimeCreate(CreateView):
    model = Anime
    fields = '__all__'

class AnimeUpdate(UpdateView):
    model = Anime
    fields = ['release_year', 'description', 'rating']

class AnimeDelete(DeleteView):
    model = Anime
    success_url = '/anime/'
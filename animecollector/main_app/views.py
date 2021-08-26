from django.shortcuts import render, redirect
from .models import Anime
from .forms import ReviewForm
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
    review_form = ReviewForm()
    return render(request, 'anime/detail.html', { 'anime': anime, 'review_form': review_form })

class AnimeCreate(CreateView):
    model = Anime
    fields = '__all__'

class AnimeUpdate(UpdateView):
    model = Anime
    fields = ['release_year', 'description', 'rating']

class AnimeDelete(DeleteView):
    model = Anime
    success_url = '/anime/'

def add_review(request, anime_id):
    form = ReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.anime_id = anime_id
        new_review.save()
    return redirect('detail', anime_id=anime_id)
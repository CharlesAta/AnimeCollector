from django.shortcuts import render, redirect
from .models import Anime, Merch
from .forms import ReviewForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class AnimeCreate(LoginRequiredMixin, CreateView):
    model = Anime
    fields = '__all__'

    def form_valid(Self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class AnimeUpdate(LoginRequiredMixin, UpdateView):
    model = Anime
    fields = ['release_year', 'description', 'rating']

class AnimeDelete(LoginRequiredMixin, DeleteView):
    model = Anime
    success_url = '/anime/'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def anime_index(request):
    anime = Anime.objects.all()
    return render(request, 'anime/index.html', { 'anime': anime })

def anime_detail(request, anime_id):
    anime = Anime.objects.get(id=anime_id)
    merch_not_in_anime = Merch.objects.exclude(id__in = anime.merch.all().values_list('id'))
    review_form = ReviewForm()
    return render(request, 'anime/detail.html', { 
        'anime': anime, 'review_form': review_form,
        'merch': merch_not_in_anime    
    })

@login_required
def add_review(request, anime_id):
    form = ReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.anime_id = anime_id
        new_review.save()
    return redirect('detail', anime_id=anime_id)

@login_required
def assoc_merch(request, anime_id, merch_id):
    Anime.objects.get(id=anime_id).merch.add(merch_id)
    return redirect('detail', anime_id=anime_id)

@login_required
def unassoc_merch(request, anime_id, merch_id):
    Anime.objects.get(id=anime_id).merch.remove(merch_id)
    return redirect('detail', anime_id=anime_id)

class MerchList(ListView):
    model = Merch

class MerchDetail(DetailView):
    model = Merch

class MerchCreate(LoginRequiredMixin, CreateView):
    model = Merch
    fields = '__all__'

class MerchUpdate(LoginRequiredMixin, UpdateView):
    model = Merch
    fields = ['name', 'price']

class MerchDelete(LoginRequiredMixin, DeleteView):
    model = Merch
    success_url = '/merch/'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationFrom(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(Request, 'registration/signup.html', context)


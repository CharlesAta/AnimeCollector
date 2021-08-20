from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

class Anime:
    def __init__(self, title, release_year, description, rating):
        self.title = title
        self.release_year = release_year
        self.description = description
        self.rating = rating

anime = [
    Anime(
        'My Hero Academia',
        2016,
        'After he saves a bully from a Villain,' \
        'a normal student is granted a superpower that' \
        ' allows him to attend a high school training academy' \
        ' for Heroes.',
        9
        ),
    Anime(
        'Haikyuu',
        2015,
        "Hinata Shouyou, a short middle school student," \
        " gained a sudden love of volleyball after watching" \
        " a national championship match on TV. Determined to" \
        " become like the championship's star player, a short" \
        " boy nicknamed 'the small giant', Shouyou joined his" \
        " school's volleyball club.",
        10
        ),
    Anime(
        'Odd Taxi',
        2021,
        'Set in a world of anthropomorphic animals, Odd Taxi' \
        ' follows the story of Odokawa, a 41-year old walrus' \
        ' taxi driver whose parents abandoned him in' \
        ' elementary school, leaving him generally asocial.',
        9
        ),
    
]

def home(request):
    return HttpResponse('<h1>Hello (ง ͡ʘ ͜ʖ ͡ʘ)ง</h1>')

def about(request):
    return render(request, 'about.html')

def anime_index(request):
    return render(request, 'anime/index.html', { 'anime': anime })
from django.contrib import admin
from .models import Anime, Review, Merch

# Register your models here.
admin.site.register(Anime)
admin.site.register(Review)
admin.site.register(Merch)
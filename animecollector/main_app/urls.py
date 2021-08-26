from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('anime/', views.anime_index, name='index'),
    path('anime/<int:anime_id>/', views.anime_detail, name='detail'),
    path('anime/create/', views.AnimeCreate.as_view(), name='anime_create'),
    path('anime/<int:pk>/update/', views.AnimeUpdate.as_view(), name='anime_update'),
    path('anime/<int:pk>/delete/', views.AnimeDelete.as_view(), name='anime_delete'),
    path('anime/<int:anime_id>/add_review/', views.add_review, name='add_review'),
]


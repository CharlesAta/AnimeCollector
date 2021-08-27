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
    path('anime/<int:anime_id>/assoc_merch/<int:merch_id>/', views.assoc_merch, name='assoc_merch'),
    path('anime/<int:anime_id>/unassoc_merch/<int:merch_id>/', views.unassoc_merch, name='unassoc_merch'),
    path('merch/', views.MerchList.as_view(), name='merch_index'),
    path('merch/<int:pk>/', views.MerchDetail.as_view(), name='merch_detail'),
    path('merch/create/', views.MerchCreate.as_view(), name='merch_create'),
    path('merch/<int:pk>/update/', views.MerchUpdate.as_view(), name='merch_update'),
    path('merch/<int:pk>/delete/', views.MerchDelete.as_view(), name='merch_delete'),
    path('accounts/signup/', views.signup, name='signup')
]


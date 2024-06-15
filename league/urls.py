from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.league_view, name='league'),
    path('create_league/', views.create_league, name='create_league'),
    path('league_list/', views.league_list_view, name='league_list'),
    path('league_edit/<str:league_id>/', views.league_edit, name='league_edit'),
    path('league_delete/<str:league_id>/', views.league_delete, name='league_delete'),
]
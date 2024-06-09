from django.urls import path
from . import views

urlpatterns = [
    path('player/', views.player_view, name='player'),
    path('player/create_player', views.player_create, name='create_player'),
    path('player/list', views.player_list_view, name='player_list'),
    path('player/edit/<str:player_id>', views.player_edit_view, name='player_edit'),
    path('player/delete/<str:player_id>', views.player_delete_view, name='player_delete'),
]

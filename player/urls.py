from django.urls import path
from . import views

urlpatterns = [
    path('', views.player_view, name='player'),
    path('create_player', views.player_create, name='create_player'),
    path('list', views.player_list_view, name='player_list'),
    path('edit/<str:player_id>', views.player_edit_view, name='player_edit'),
    path('delete/<str:player_id>', views.player_delete, name='player_delete'),
    path('player_reject/', views.player_reject, name='player_reject'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('league/<int:league_id>/', views.league_detail, name='league_detail'),
    path('league/<int:league_id>/create/', views.match_create, name='match_create'),
    path('match/<int:match_id>/update/', views.match_update, name='match_update'),
    path('match/<int:match_id>/edit/', views.match_edit, name='match_edit'),
    path('match/<int:match_id>/delete/', views.match_delete, name='match_delete'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('league/<str:league_id>/', views.league_detail, name='league_detail'),
    path('league/<str:league_id>/create/', views.match_create, name='match_create'),
    path('match/<str:match_id>/update/', views.match_update, name='match_update'),
    path('match/<str:match_id>/edit/', views.match_edit, name='match_edit'),
    path('match/<str:match_id>/delete/', views.match_delete, name='match_delete'),
]
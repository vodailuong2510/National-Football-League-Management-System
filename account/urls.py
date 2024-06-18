from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', views.register, name='register'),
    path('change_password/', views.change_password, name='change_password'),
    path('edit_profile/', views.edit_profile, name = 'edit_profile'),
    path('profile/', views.profile, name = 'profile'),
    path('toggle_follow_player/<int:player_id>/', views.toggle_follow_player_profile, name='toggle_follow_player_profile'),
    path('toggle_follow_league/<int:league_id>/', views.toggle_follow_league_profile, name='toggle_follow_league_profile'),
    path('toggle_follow_club/<int:club_id>/', views.toggle_follow_club_profile, name='toggle_follow_club_profile'),
    path('toggle_follow_coach/<int:coach_id>/', views.toggle_follow_coach_profile, name='toggle_follow_coach_profile'),
    path('profile/followed_league', views.followed_league, name='followed_league'),
]
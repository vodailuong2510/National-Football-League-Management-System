from django.urls import path
from . import views

urlpatterns = [
    path('', views.club_view, name='club'),
    path('create_club/', views.create_club, name='create_club'),
    path('club_list/', views.club_list, name='club_list'),
    path('club_edit/<str:club_id>/', views.club_edit, name='club_edit'),
    path('club_delete/<str:club_id>/', views.club_delete, name='club_delete'),
    path('club_reject/', views.club_reject, name='club_reject'),
    path('toggle_follow/<int:club_id>/', views.toggle_follow_club, name='toggle_follow_club'),
]
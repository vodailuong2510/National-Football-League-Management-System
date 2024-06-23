from django.urls import path
from . import views

urlpatterns = [
    path('', views.coach_view, name='coach'),
    path('create_coach/', views.coach_create, name='create_coach'),
    path('list/', views.coach_list_view, name='coach_list'),
    path('edit/<str:coach_id>/', views.coach_edit_view, name='coach_edit'),
    path('delete/<str:coach_id>/', views.coach_delete_view, name='coach_delete'),
    path('coach_reject/', views.coach_reject, name='coach_reject'),
    path('toggle_follow/<str:coach_id>/', views.toggle_follow_coach, name='toggle_follow_coach'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('coach/', views.coach_view, name='coach'),
    path('coach/create_coach', views.coach_create, name='create_coach'),
    path('coach/list', views.coach_list_view, name='coach_list'),
    path('coach/edit/<str:coach_id>', views.coach_edit_view, name='coach_edit'),
    path('coach/delete/<str:coach_id>', views.coach_delete_view, name='coach_delete'),
]

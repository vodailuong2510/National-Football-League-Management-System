from django.urls import path
from . import views

urlpatterns = [
    path('coach/', views.coach_view, name='coach'),
]

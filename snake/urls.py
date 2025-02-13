from django.urls import path
from . import views

urlpatterns = [
    path('', views.snake, name='snake'),  # Add this line for the empty path
    path('snake/', views.snake, name='snake'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('snake/', views.snake, name='snake'),
    path('submit_score/', views.submit_score, name='submit_score'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('tictactoe/', views.tictactoe, name='tictactoe'),
    path('game/<str:game_name>/', views.game_welcome, name='game_welcome'),
    path('tictacindex/', views.tictacindex, name='tictacindex'),   
]
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Game, Leaderboard

def index(request):
    return render(request, 'snake/index.html')

def snake(request):
    return render(request, 'snake/snake.html')

@login_required
@csrf_exempt
def submit_score(request):
    if request.method == "POST":
        score_value = int(request.POST.get("score", 0))
        user = request.user
        Score.objects.create(user=user, score=score_value)
        return redirect('leaderboard')  # Redirect to the leaderboard page or any other page
    return redirect('game')  # Redirect to the game page if the request method is not POST

@login_required
def leaderboard(request):
    scores = Score.objects.order_by('-score')[:10]  # Get top 10 scores
    return render(request, 'snake/leaderboard.html', {'scores': scores})

@login_required
def tictactoe(request):
    return render(request, 'snake/tictactoe.html')

def home(request):
    return render(request, 'home.html')
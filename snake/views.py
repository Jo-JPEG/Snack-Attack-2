from django.shortcuts import render, render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Game, GameSession, Leaderboard

def index(request):
    return render(request, 'snake/index.html')

def snake(request):
    # Fetch top 10 scores per game
    leaderboard_data = (
        Leaderboard.objects.order_by('-highest_score')
        .select_related('user', 'game')[:10]
    )
    return render(request, 'snake/snake.html', {'leaderboard': leaderboard_data})

@login_required
@csrf_exempt
def submit_score(request):
    if request.method == "POST":
        score_value = int(request.POST.get("score", 0))
        game_name = request.POST.get("game")  # Ensure the frontend sends 'game' in POST data
        user = request.user

        try:
            game = Game.objects.get(name=game_name)
        except Game.DoesNotExist:
            return JsonResponse({"error": "Game not found"}, status=400)

        # Save the new game session
        session = GameSession.objects.create(user=user, game=game, score=score_value)

        # Update leaderboard
        leaderboard_entry, created = Leaderboard.objects.get_or_create(user=user, game=game)
        if created:
            leaderboard_entry.highest_score = session.score
        elif session.score > leaderboard_entry.highest_score:
            leaderboard_entry.highest_score = session.score
        leaderboard_entry.save()

        return redirect('leaderboard')  # Redirect to the leaderboard page

    return redirect('game')  # Redirect to game page if request is not POST

@login_required
def leaderboard(request):
    # Fetch top 10 scores per game
    leaderboard_data = (
        Leaderboard.objects.order_by('-highest_score')
        .select_related('user', 'game')[:10]
    )
    return render(request, 'snake/leaderboard.html', {'leaderboard': leaderboard_data})

@login_required
def tictactoe(request):
    return render(request, 'snake/tictactoe.html')

def home(request):
    games = Game.objects.all()
    return render(request, 'home.html', {'game_list': games})

def game_welcome(request, game_name):
    game = get_object_or_404(Game, name=game_name)
    template_name = f'{game_name.lower()}/index.html'
    return render(request, template_name, {'game': game})
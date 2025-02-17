from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

class Game(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='static/snake', blank=True)

    def __str__(self):
        return self.name

class GameSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    score = models.IntegerField()
    date_played = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} scored {self.score} in {self.game.name} on {self.date_played}'

class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    highest_score = models.IntegerField()
    ranking = models.IntegerField()

    class Meta:
        unique_together = ('user', 'game')  # A user can have one leaderboard entry per game

    def __str__(self):
        return f"{self.user.username}: {self.highest_score} in {self.game.name} (Rank {self.ranking})"

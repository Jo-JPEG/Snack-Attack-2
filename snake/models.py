from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    date_played = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='static/snake', blank=True)

    def __str__(self):
        return f'{self.user.username} scored {self.score} on {self.date_played}'

class Leaderboard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    highest_score = models.IntegerField()
    ranking = models.IntegerField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}: {self.highest_score} in {self.game.name}"


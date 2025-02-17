from django.contrib import admin
from .models import Profile, Game, GameSession, Leaderboard

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    search_fields = ('name',)

@admin.register(GameSession)
class GameSessionAdmin(admin.ModelAdmin):
    list_display = ('user', 'game', 'score', 'date_played')
    list_filter = ('game', 'date_played')
    search_fields = ('user__username', 'game__name')

@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ('user', 'game', 'highest_score')
    list_filter = ('game',)
    search_fields = ('user__username', 'game__name')
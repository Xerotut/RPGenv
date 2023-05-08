from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.core import serializers
from django.http import JsonResponse
from .models import Game
# Create your views here.

class GameListView(ListView):
    template_name = "mythic/games_list.html"
    context_object_name = "games"

    def get_queryset(self):
        return Game.objects.all()
    

def game_view(request, game_id):
    game = get_object_or_404(Game, pk = game_id)
    context = {"game": game}
    return render (request, 'mythic/game.html', context)

def get_more_games(request):
    games = Game.objects.all()
    serialized_games = serializers.serialize('json', games)
    return JsonResponse(serialized_games, safe=False)
    
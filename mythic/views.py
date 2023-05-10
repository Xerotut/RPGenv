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

def get_more_games(request, created_next):
    print(created_next)
    game = Game.objects.order_by('id')[created_next:created_next+1]
    serialized_game = serializers.serialize('json', game)
   # print(serialized_game)
    return JsonResponse(serialized_game, safe=False)
    
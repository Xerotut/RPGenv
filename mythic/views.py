from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.generic.list import ListView
from django.core import serializers
from django.http import JsonResponse
from .models import Game, MeaningTable, Scene, SceneMessage, Note
import json
from django.views.decorators.csrf import csrf_protect

from django.db.models import F
# Create your views here.

class GameListView(ListView):
    template_name = "mythic/games_list.html"
    context_object_name = "games"

    def get_queryset(self):
        return Game.objects.all()
    

def game_view(request, game_id):
    game = get_object_or_404(Game, pk = game_id)
    meaning_tables = MeaningTable.objects.filter(type = "ELEMENT")
    scenes = Scene.objects.filter(game = game_id)
    context = {"game": game, "meaning_tables":meaning_tables, "scenes": scenes}
    return render (request, 'mythic/game.html', context)

def show_games_list(request):
    if request.method == "POST":
        name = request.POST.get('new-game-name')
        games_to_serialize = Game(name = name)
        games_to_serialize.save()
        serialized_games = serializers.serialize('json', [games_to_serialize])
    else:
        games_to_serialize = Game.objects.all()
        serialized_games = serializers.serialize('json', games_to_serialize)
    
    return JsonResponse(serialized_games, safe=False)
        

def get_more_games(request):
    print(json.loads(request.body))
    data = json.loads(request.body)

    games_displayed = data.get('games_displayed')
    game = Game.objects.order_by('id')[games_displayed:games_displayed+1]
    serialized_game = serializers.serialize('json', game)
    print(serialized_game)
    return JsonResponse(serialized_game, safe=False)
    
def messages(request,game_id, scene_id):
    if request.method == "GET":
        if scene_id !=0:
            try:
                game = get_object_or_404(Game, pk=game_id)
                scene = get_object_or_404(Scene, pk=scene_id, game=game)
                messages = SceneMessage.objects.filter(scene=scene).order_by('-time_created')[:5]
            except Http404:
                print('halo')
        else:
            print("halo")
            messages = Note.objects.filter(game=game_id).order_by('-time_created')[:5]
        seralized_messages = serializers.serialize('json', messages)
        return JsonResponse(seralized_messages, safe=False)
    else:
        message = request.POST.get('message')
        game = get_object_or_404(Game, pk=game_id)
        if scene_id !=0:
            scene = get_object_or_404(Scene, pk=scene_id, game=game)
            new_message = SceneMessage(text = message, scene = scene)
        else:
            new_message = Note(text = message, game = game)
        new_message.save()
        print(message)
        return None
    

@csrf_protect
def delete_game(request,game_id):
    game = get_object_or_404(Game, pk = game_id)
    game.delete()

def send_message(request):
    print("halo")
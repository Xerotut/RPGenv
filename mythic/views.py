from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import JsonResponse, Http404
from.scripts import serialize_data_to_json
from .forms import GameForm
from django.template.response import TemplateResponse
from django.template.loader import render_to_string
from .models import Game, MeaningTable, Scene, SceneMessage, Note, List, ListNote
from django.views.decorators.csrf import csrf_protect

# Create your views here.
@csrf_protect
def mythic_games_page(request):
    user = request.user
    if request.method == "POST":
        form = GameForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            name = form.cleaned_data.get('name')
            new_game = Game(user = user, name = name)
            new_game.save()
            new_game_context = {"game": new_game}
            html = render_to_string("mythic/game_list_entry_template.html", new_game_context)
            data = {
            'html': html,
            'game_id':new_game.pk,
            }
            return JsonResponse(data)
    form = GameForm()
    games = Game.objects.filter(user=user)
    context = {'games':games, 'new_game_form': form}
    return render(request,'mythic/games_list.html', context)

def delete_game(request, game_id):
    if request.method == "DELETE":
        user = request.user
        print(game_id)
        try:
            game = get_object_or_404(Game, pk = game_id)
            if game.user == user:
                game.delete()
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, "error": "You don't have ownership over this game."})
        except Http404:
            return JsonResponse({'success': False, 'error': 'Game does not exist'})

def game_view(request, game_id):
    game = get_object_or_404(Game, pk = game_id)
    meaning_tables = MeaningTable.objects.filter(type = "ELEMENT")
    scenes = Scene.objects.filter(game = game_id)
    context = {"game": game, "meaning_tables":meaning_tables, "scenes": scenes}
    return render (request, 'mythic/game.html', context)

def messages(request,game_id, scene_id):
    game = get_object_or_404(Game, pk=game_id)
    scene = get_object_or_404(Scene, pk=scene_id, game=game)
    if request.method == "GET":
        game.active_scene = scene
        messages = SceneMessage.objects.filter(scene=scene).order_by('-time_created')[:5][::-1]
        game.save()
        seralized_data = serialize_data_to_json(messages)
        print(seralized_data)
    else:
        message = request.POST.get('message')
        print(message)
        new_message = SceneMessage(text = message, scene = scene)
        new_message.save()
        seralized_data = serialize_data_to_json([new_message])
        print(seralized_data)
    return JsonResponse(seralized_data, safe=False)

def notes(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    if request.method == "GET":
        notes =  Note.objects.filter(game=game).order_by('-time_created')[:5][::-1]
        serialized_data = serialize_data_to_json(notes)
    else:
        note = request.POST.get('note')
        new_note = Note(text = note, game = game)
        new_note.save()
        serialized_data = serialize_data_to_json([new_note])
        return None
    return JsonResponse(serialized_data, safe=False)

def scenes(request, game_id):
    game = get_object_or_404(Game, pk =game_id)
    if request.method == "POST":
        scene_data = request.POST.get('scene')
        new_scene = Scene(game = game, name = scene_data.name)
        new_scene.save()
        serialized_data = serialize_data_to_json(new_scene)
    return JsonResponse(serialized_data, safe=False)

def lists_entries(request, list_id):
    list =get_object_or_404(List, pk = list_id)
    if request.method == "GET":
        entries = ListNote.objects.filter(note_list = list)
        serialized_data = serialize_data_to_json(entries)
    else:
        new_entry_data =  request.POST.get('entry')
        new_entry = ListNote(note_list = list, name = new_entry_data.name, text = new_entry_data.text)
        new_entry.save()
        serialized_data = serialize_data_to_json([new_entry])
    return JsonResponse(serialized_data, safe=False)
"""         
def meaning_roll_action(request ):

def meaning_roll_description(request):

def meaning_roll_element(request, table_id):
 """

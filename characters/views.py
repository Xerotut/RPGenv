from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Character

# Create your views here.

app_name = "characters"
def character_list(request):
    characters = Character.objects.all()
    context = {"characters" : characters}
    return render(request, "characters/character_list.html", context)

def character_sheet(request, character_id):
    character = get_object_or_404(Character, pk= character_id)    
    return render(request, "characters/character_sheet.html", {"character": character})
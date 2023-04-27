from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views import generic

from .models import Character

# Create your views here.



class CharIndexView(generic.ListView):
    template_name = "characters/character_list.html"
    context_object_name = "characters"

    def get_queryset(self):
        return Character.objects.all()
    
class CharSheetView(generic.DetailView):
    model = Character
    template_name = "characters/character_sheet.html"

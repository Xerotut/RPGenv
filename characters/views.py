from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Character, CharAttribute
from .forms import CharacterForm, CharAttributeForm
# Create your views here.



class CharIndexView(generic.ListView):
    template_name = "characters/character_list.html"
    context_object_name = "characters"

    def get_queryset(self):
        return Character.objects.all()
    
class CharSheetView(generic.DetailView):
    model = Character
    template_name = "characters/character_sheet.html"

def character_sheet(request, pk):
    character = get_object_or_404(Character, pk=pk)
    attributes = CharAttribute.objects.filter(character = character)
    
    if request.method == 'POST':
      
        attribute_forms = [CharAttributeForm(request.POST, instance=attribute, prefix=f'attribute_{attribute.pk}') for attribute in attributes]
        form = CharacterForm(request.POST, instance = character)
        
        if form.is_valid() and all(attribute_form.is_valid() for attribute_form in attribute_forms):         
            form.save()    
            for attribute_form in attribute_forms:              
                attribute_form.save()
    
    attribute_forms = [CharAttributeForm(instance=attribute, prefix=f'attribute_{attribute.pk}') for attribute in attributes]
    form = CharacterForm(instance=character)
    context = {'character': character,'form':form, 'attribute_forms': attribute_forms}
    return render(request, "characters/character_sheet.html", context)

    
    
    
def save_character(request, character_id):
    character = get_object_or_404(Character, pk=character_id)
    character.name = request.POST['character_name']
    character.level = request.POST['character_level']
    character.current_exp = request.POST['character_exp']
    for attribute in character.charattribute_set.all():        
        attribute.value = request.POST[str(attribute.attribute.name)]
        attribute.save()
    for skill in character.charskill_set.all():
        skill.allocated_points = request.POST[str(skill.skill.name)]
        skill.save()
    character.save()
    return HttpResponseRedirect(reverse("characters:character_sheet", args = (character.id,)))


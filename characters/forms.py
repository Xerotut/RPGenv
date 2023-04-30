from django.forms import ModelForm
from .models import Character


class CharacterModel(ModelForm):
    model = Character
    fields = "__all__"
from django.forms import ModelForm
from .models import Character


class CharacterForm(ModelForm):
    model = Character
    fields = "__all__"
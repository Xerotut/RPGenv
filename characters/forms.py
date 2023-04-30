from django import forms
from .models import Character, Attribute, CharAttribute


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = "__all__"


class CharAttributeForm(forms.ModelForm):
    class Meta:
        model = CharAttribute
        fields = ['attribute', 'value']
       


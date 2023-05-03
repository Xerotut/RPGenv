from django import forms
from .models import Character, Attribute, CharAttribute


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        exclude = ['skills', 'attributes']
    

class CharAttributeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['value'].label = self.instance.attribute.name

    class Meta:
        model = CharAttribute
        fields = ['value']
       
        
    
       


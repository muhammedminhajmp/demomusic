from django import forms
from . models import music

class MusicForm(forms.ModelForm):
    class Meta:
        model=music
        fields=['name','desc','year','img']
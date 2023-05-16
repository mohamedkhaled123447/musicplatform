from django import forms
from .models import Artist
class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields ="__all__"
        error_messages={
            'name':{
                'required':'Please enter the name of the artist',
                 'unique':'Artist already exists'
                },
        }
    
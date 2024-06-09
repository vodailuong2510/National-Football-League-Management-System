from django import forms
from .models import Player

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['PLAYERID', 'PLAYERNAME', 'BIRTHDAY', 'NATIONALITY', 'CLUB', 'IMAGE', 'CARDS']
    
    def __init__(self, *args, **kwargs):
        super(PlayerForm, self).__init__(*args, **kwargs)
        self.fields['PLAYERID'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Mã Cau thu'})
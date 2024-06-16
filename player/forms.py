from django import forms
from .models import Player

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['PLAYERID', 'PLAYERNAME', 'BIRTHDAY', 'NATIONALITY', 'CLUB', 'IMAGE', 'CARDS']
    
    def __init__(self, *args, **kwargs):
        disable_playerid = kwargs.pop('disable_playerid', False)
        super(PlayerForm, self).__init__(*args, **kwargs)
        
        self.fields['PLAYERID'].widget.attrs.update({'class': 'form-control'})
        for field_name in self.fields:
            if field_name != 'CARDS':
                self.fields[field_name].widget.attrs.update({'class': 'my-input'})
                
        if disable_playerid:
            self.fields['PLAYERID'].disabled = True
                
    def check_id(self, PLAYERID):
        if Player.objects.filter(PLAYERID=PLAYERID).exists():
            raise forms.ValidationError('ID already exists')
        return PLAYERID
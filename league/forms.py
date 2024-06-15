from django import forms
from .models import League

class LeagueForm(forms.ModelForm):
    class Meta:
        model = League
        fields = ['LEAGUE_ID', 'LEAGUE_NAME', 'ASSOCIATION', 'FOUNDED', 'START_TIME', 'END_TIME']
    
    def __init__(self, *args, **kwargs):
        disable_league_id = kwargs.pop('disable_league_id', False)
        super(LeagueForm, self).__init__(*args, **kwargs)
        
        self.fields['LEAGUE_ID'].widget.attrs.update({'class': 'form-control'})
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': 'my-input'})
                
        if disable_league_id:
            self.fields['LEAGUE_ID'].disabled = True
                
    def check_id(self, LEAGUE_ID):
        if League.objects.filter(LEAGUE_ID=LEAGUE_ID).exists():
            raise forms.ValidationError('ID already exists')
        return LEAGUE_ID

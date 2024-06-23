from django import forms
from .models import League

class LeagueForm(forms.ModelForm):
    class Meta:
        model = League
        fields = ['LEAGUE_ID', 'LOGO', 'TOTAL_CLUB', 'ASSOCIATION', 'FOUNDED', 'START_TIME', 'END_TIME']
    
    def __init__(self, *args, **kwargs):
        disable_league_id = kwargs.pop('disable_league_id', False)
        super(LeagueForm, self).__init__(*args, **kwargs)
        
        self.fields['LEAGUE_ID'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Tên giải đấu'})
        self.fields['LOGO'].widget.attrs.update({'class': 'my-input', 'placeholder': 'Logo'})
        self.fields['TOTAL_CLUB'].widget.attrs.update({'class': 'my-input', 'placeholder': 'Số đội bóng'})
        self.fields['ASSOCIATION'].widget.attrs.update({'class': 'my-input', 'placeholder': 'Hiệp hội'})
        self.fields['FOUNDED'].widget.attrs.update({'class': 'my-input', 'placeholder': 'mm/dd/YYYY'})
        self.fields['START_TIME'].widget.attrs.update({'class': 'my-input', 'placeholder': 'mm/dd/YYYY'})
        self.fields['END_TIME'].widget.attrs.update({'class': 'my-input', 'placeholder': 'mm/dd/YYYY'})
                
        if disable_league_id:
            self.fields['LEAGUE_ID'].disabled = True
                
    def check_id(self, LEAGUE_ID):
        if League.objects.filter(LEAGUE_ID=LEAGUE_ID).exists():
            raise forms.ValidationError('ID already exists')
        return LEAGUE_ID

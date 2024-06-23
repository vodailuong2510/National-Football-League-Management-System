from django import forms
from .models import Match
from club.models import Club

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['MATCHID', 'LEAGUEID', 'HOMETEAM', 'AWAYTEAM', 'ROUND', 'DATE', 'TIME', 'STADIUM', 'REFEREE']

    def __init__(self, *args, **kwargs):
        league = kwargs.pop('league', None)
        super(MatchForm, self).__init__(*args, **kwargs)
        self.fields['MATCHID'].widget.attrs.update({'class': 'form-control', 'placeholder': 'ID trận đấu'})
        self.fields['LEAGUEID'].widget.attrs.update({'class': 'my-input', 'placeholder': 'ID giải đấu'})
        self.fields['HOMETEAM'].widget.attrs.update({'class': 'my-input', 'placeholder': 'Đội nhà'})
        self.fields['AWAYTEAM'].widget.attrs.update({'class': 'my-input', 'placeholder': 'Đội khách'})
        self.fields['ROUND'].widget.attrs.update({'class': 'my-input', 'placeholder': 'Vòng đấu'})
        self.fields['DATE'].widget.attrs.update({'class': 'my-input', 'placeholder': 'dd/mm/YYYY'})
        self.fields['TIME'].widget.attrs.update({'class': 'my-input', 'placeholder': 'hh:mm'})
        self.fields['STADIUM'].widget.attrs.update({'class': 'my-input', 'placeholder': 'Sân vận động'})
        self.fields['REFEREE'].widget.attrs.update({'class': 'my-input', 'placeholder': 'Trọng tài'})
        
        if league:
            self.fields['HOMETEAM'].queryset = Club.objects.filter(LEAGUEPLAYING=league.LEAGUE_NAME)
            self.fields['AWAYTEAM'].queryset = Club.objects.filter(LEAGUEPLAYING=league.LEAGUE_NAME)

class ScoreForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['HOMESCORE', 'AWAYSCORE']
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
        if league:
            self.fields['HOMETEAM'].queryset = Club.objects.filter(LEAGUEPLAYING=league.LEAGUE_NAME)
            self.fields['AWAYTEAM'].queryset = Club.objects.filter(LEAGUEPLAYING=league.LEAGUE_NAME)

class ScoreForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['HOMESCORE', 'AWAYSCORE']
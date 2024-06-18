from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Match, Ranking
from .forms import MatchForm, ScoreForm
from league.models import League
from club.models import Club
from django.contrib import messages
# Create your views here.
def league_detail(request, league_id):
    league = get_object_or_404(League, LEAGUE_ID=league_id)
    clubs = Club.objects.filter(LEAGUEPLAYING=league.LEAGUE_NAME)
    matches = Match.objects.filter(LEAGUEID=league)
    rankings = Ranking.objects.filter(LEAGUE=league).select_related('CLUB')
    return render(request, 'league_detail.html', {'league': league, 'clubs': clubs, 'matches': matches, 'rankings': rankings})

def match_create(request, league_id):
    league = get_object_or_404(League, LEAGUE_ID=league_id)
    clubs = Club.objects.filter(LEAGUEPLAYING=league.LEAGUE_NAME)
    if request.method == 'POST':
        form = MatchForm(request.POST, league=league)
        if form.is_valid():
            form.save()
            return redirect('league_detail', league_id=league.LEAGUE_ID)
        else:
            print(form.errors)
    else:
        form = MatchForm(league=league)
    return render(request, 'match_create.html', {'form': form, 'league': league, 'clubs': clubs})

def match_update(request, match_id):
    match_instance = get_object_or_404(Match, MATCHID=match_id)
    if request.method == 'POST':
        form = ScoreForm(request.POST, instance=match_instance)
        if form.is_valid():
            form.save()
            return redirect('league_detail', league_id=match_instance.LEAGUEID.LEAGUE_ID)
    else:
        form = ScoreForm(instance=match_instance)
    return render(request, 'match_update.html', {'form': form, 'match_instance': match_instance})

def match_edit(request, match_id):
    match = get_object_or_404(Match, MATCHID=match_id)
    league = match.LEAGUEID
    if request.method == 'POST':
        form = MatchForm(request.POST, instance=match, league=league)
        if form.is_valid():
            new_match_id = form.cleaned_data['MATCHID']
            if new_match_id != match_id and Match.objects.filter(MATCHID=new_match_id).exists():
                form.add_error('MATCHID', 'ID trận đấu đã tồn tại')
            else:
                form.save()
                return redirect('league_detail', league_id=league.LEAGUE_ID)
        else:
            print(form.errors)
    else:
        form = MatchForm(instance=match, league=league)
    return render(request, 'match_edit.html', {'form': form, 'league': league})

def match_delete(request, match_id):
    match = get_object_or_404(Match, MATCHID=match_id)
    league_id = match.LEAGUEID.LEAGUE_ID
    if request.method == 'POST':
        match.delete()
        return redirect('league_detail', league_id=league_id)
    return render(request, 'match_delete.html', {'match': match})
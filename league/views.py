from django.shortcuts import render, redirect, get_object_or_404
from .forms import LeagueForm
from .models import League
from django.contrib import messages

# Create your views here.
def create_league(request):
    if request.method == 'POST':
        form = LeagueForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, ' ')
        else:
            print(form.errors)
    else:
        form = LeagueForm()
    return render(request, 'create_league.html', {'form': form})

def league_list_view(request):
    leagues = League.objects.all()
    # Xử lý yêu cầu tìm kiếm
    search_query = request.GET.get('search')
    if search_query:
        leagues = leagues.filter(LEAGUE_NAME__icontains=search_query)
    return render(request, 'league_list.html', {'leagues': leagues})

def league_edit(request, league_id):
    league = get_object_or_404(League, LEAGUE_ID=league_id)
    
    if request.method == 'POST':
        form = LeagueForm(request.POST, request.FILES, instance=league)
        if form.is_valid():
            new_league_id = form.cleaned_data['LEAGUE_ID']
            if new_league_id != league_id and League.objects.filter(LEAGUE_ID=new_league_id).exists():
                form.add_error('LEAGUE_ID', 'ID đã tồn tại')
            else:
                form.save()
                return redirect('league_list')
        else:
            print(form.errors)
    else:
        form = LeagueForm(instance=league)
    
    return render(request, 'edit_league.html', {'form': form})

def league_delete(request, league_id):
    league = get_object_or_404(League, LEAGUE_ID=league_id)
    
    if request.method == 'POST':
        league.delete()
        return redirect('league_list')
    
    return render(request, 'delete_league.html', {'league': league})
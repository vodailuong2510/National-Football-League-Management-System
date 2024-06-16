from django.shortcuts import render, redirect, get_object_or_404
from .forms import LeagueForm
from .models import League
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

# Create your views here.
def league_view(request):
    leagues = League.objects.all() 
    return render(request, 'league.html', {'leagues': leagues})

@login_required
def create_league(request):
    if request.method == 'POST':
        form = LeagueForm(request.POST, request.FILES)
        if form.is_valid():
            league = form.save(commit=False)
            league.owner = request.user  # Lưu người dùng hiện tại là chủ sở hữu
            league.save()
            messages.success(request, 'Bạn đã đăng ký giải đấu thành công.')
            return redirect('league_list')
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

@login_required
def league_edit(request, league_id):
    league = get_object_or_404(League, LEAGUE_ID=league_id)
    
    # Kiểm tra xem người dùng hiện tại có phải là chủ sở hữu không
    if league.owner != request.user:
        return redirect('league_reject')
    
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

@login_required
def league_delete(request, league_id):
    league = get_object_or_404(League, LEAGUE_ID=league_id)
    
    # Kiểm tra xem người dùng hiện tại có phải là chủ sở hữu không
    if league.owner != request.user:
        return redirect('league_reject')
    
    if request.method == 'POST':
        league.delete()
        return redirect('league_list')
    
    return render(request, 'delete_league.html', {'league': league})

def league_reject(request):
    return render(request, 'league_reject.html')

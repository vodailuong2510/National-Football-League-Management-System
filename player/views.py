from django.shortcuts import render, redirect, get_object_or_404
from .forms import PlayerForm
from .models import Player

# Create your views here.
def player_view(request):
    players = Player.objects.all()
    return render(request, 'player/player.html', {'players': players})

def player_create(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('player_list')
    else:
        form = PlayerForm()
    return render(request, 'player/create_player.html', {'form': form})

def player_list_view(request):
    players = Player.objects.all()

    # Xử lý yêu cầu tìm kiếm
    search_query = request.GET.get('search')
    if search_query:
        players = players.filter(PLAYERNAME__icontains=search_query)

    return render(request, 'player/player_list.html', {'players': players})

def player_edit_view(request, player_id):
    player = get_object_or_404(Player, PLAYERID=player_id)

    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES, instance=player)
        if form.is_valid():
            form.save()
            return redirect('player_list')
    else:
        form = PlayerForm(instance=player)

    return render(request, 'player/edit_player.html', {'form': form})

def player_delete_view(request, player_id):
    player = get_object_or_404(Player, PLAYERID=player_id)
    player.delete()
    return redirect('player_list')
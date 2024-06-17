from django.shortcuts import render, redirect, get_object_or_404
from .forms import PlayerForm
from .models import Player
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

def player_view(request):
    players = Player.objects.all()
    return render(request, 'player/player.html', {'players': players})

@login_required
def player_create(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES)
        if form.is_valid():
            player = form.save(commit=False)
            player.owner = request.user  # Lưu người dùng hiện tại là chủ sở hữu
            player.save()
            messages.success(request, 'Đăng ký thành công.')
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

@login_required
def player_edit_view(request, player_id):
    player = get_object_or_404(Player, PLAYERID=player_id)

    # Kiểm tra xem người dùng hiện tại có phải là chủ sở hữu không
    if player.owner != request.user:
        return redirect('player_reject')

    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES, instance=player)
        if form.is_valid():
            form.save()
            return redirect('player_list')
    else:
        form = PlayerForm(instance=player)

    return render(request, 'player/edit_player.html', {'form': form})

@login_required
def player_delete(request, player_id):
    player = get_object_or_404(Player, PLAYERID=player_id)

    # Kiểm tra xem người dùng hiện tại có phải là chủ sở hữu không
    if player.owner != request.user:
        return redirect('player_reject')

    if request.method == 'POST':
        player.delete()
        return redirect('player_list')

    return render(request, 'player/delete_player.html', {'player': player})

@login_required
def player_reject(request):
    return render(request, 'player/player_reject.html')
@login_required
def toggle_follow(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    user = request.user

    if user in player.followers.all():
        player.followers.remove(user)
    else:
        player.followers.add(user)

    return redirect('player')
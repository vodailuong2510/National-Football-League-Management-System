from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponseRedirect
from .forms import RegistrationForm
from django.urls import reverse
from django.contrib import messages
from .forms import CustomPasswordChangeForm
from .forms import UserUpdateForm
from django.contrib.auth.decorators import login_required
from player.models import Player
from league.models import League
from club.models import Club
from coach.models import Coach
# Create your views here.
# views.py

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bạn đã đăng ký tài khoản thành công.')
            return HttpResponseRedirect(reverse('login'))
    return render(request, 'register.html', {'form' : form})

def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) 
            messages.success(request, 'Mật khẩu của bạn đã được thay đổi thành công!')
            return redirect(reverse('change_password')) 
        else:
            messages.error(request, 'Vui lòng kiểm tra lại thông tin.')
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})

def edit_profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thông tin tài khoản của bạn đã được cập nhật thành công!')
            return redirect(reverse('edit_profile'))
        else:
            messages.error(request, 'Vui lòng kiểm tra lại thông tin.')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})

def profile(request):
    players = Player.objects.all()
    leagues = League.objects.all()
    coaches = Coach.objects.all()
    clubs = Club.objects.all()
    return render(request, 'profile.html', {'players': players, 'leagues': leagues, 'coaches': coaches, 'clubs': clubs})

@login_required
def toggle_follow_player_profile(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    user = request.user

    if user in player.followers.all():
        player.followers.remove(user)
    else:
        player.followers.add(user)

    return redirect('profile')

@login_required
def toggle_follow_league_profile(request, league_id):
    league = get_object_or_404(League, pk=league_id)
    user = request.user

    if user in league.followers.all():
        league.followers.remove(user)
    else:
        league.followers.add(user)

    return redirect('profile')

@login_required
def toggle_follow_club_profile(request, club_id):
    club = get_object_or_404(Club, pk=club_id)
    user = request.user

    if user in club.followers.all():
        club.followers.remove(user)
    else:
        club.followers.add(user)

    return redirect('profile')

@login_required
def toggle_follow_coach_profile(request, coach_id):
    coach = get_object_or_404(Coach, pk=coach_id)
    user = request.user

    if user in coach.followers.all():
        coach.followers.remove(user)
    else:
        coach.followers.add(user)

    return redirect('profile')
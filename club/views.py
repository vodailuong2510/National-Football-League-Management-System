from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClubForm
from .models import Club
from django.contrib import messages

def create_club(request):
    if request.method == 'POST':
        form = ClubForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,' ')
        else:
            print(form.errors)
    else:
        form = ClubForm()
    return render(request, 'create_club.html', {'form': form})

def club_list(request):
    clubs = Club.objects.all()
    search_query = request.GET.get('search')
    if search_query:
        clubs = clubs.filter(CLUBNAME__icontains=search_query)
    return render(request, 'club_list.html', {'clubs': clubs})

def club_edit(request, club_id):
    club = get_object_or_404(Club, CLUBID=club_id)
    if request.method == 'POST':
        form = ClubForm(request.POST, request.FILES, instance=club)
        if form.is_valid():
            new_club_id = form.cleaned_data['CLUBID']
            if new_club_id != club_id and Club.objects.filter(CLUBID=new_club_id).exists():
                form.add_error('CLUBID', 'ID đội bóng đã tồn tại')
            else:
                form.save()
                return redirect('club_list')
        else:
            print(form.errors)
    else:
        form = ClubForm(instance=club)
    return render(request, 'edit_club.html', {'form': form})

def club_delete(request, club_id):
    club = get_object_or_404(Club, CLUBID=club_id)
    if request.method == 'POST':
        club.delete()
        return redirect('club_list')
    return render(request, 'delete_club.html', {'club': club})
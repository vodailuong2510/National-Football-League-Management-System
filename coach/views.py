from django.shortcuts import render, redirect, get_object_or_404
from .forms import CoachForm
from .models import Coach

# Create your views here.
def coach_view(request):
    coaches = Coach.objects.all()
    return render(request, 'coach/coach.html', {'coaches': coaches})

def coach_create(request):
    if request.method == 'POST':
        form = CoachForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('coach_list')
    else:
        form = CoachForm()
    return render(request, 'coach/create_coach.html', {'form': form})

def coach_list_view(request):
    coaches = Coach.objects.all()

    # Xử lý yêu cầu tìm kiếm
    search_query = request.GET.get('search')
    if search_query:
        coaches = coaches.filter(COACHNAME__icontains=search_query)

    return render(request, 'coach/coach_list.html', {'coaches': coaches})

def coach_edit_view(request, coach_id):
    coach = get_object_or_404(Coach, COACHID=coach_id)

    if request.method == 'POST':
        form = CoachForm(request.POST, request.FILES, instance=coach)
        if form.is_valid():
            form.save()
            return redirect('coach_list')
    else:
        form = CoachForm(instance=coach)

    return render(request, 'coach/edit_coach.html', {'form': form})

def coach_delete_view(request, coach_id):
    coach = get_object_or_404(Coach, COACHID=coach_id)
    coach.delete()
    return redirect('coach_list')
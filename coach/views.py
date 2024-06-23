from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CoachForm
from .models import Coach

def coach_view(request):
    coaches = Coach.objects.all()

    # Xử lý yêu cầu tìm kiếm
    search_query = request.GET.get('search')
    if search_query:
        coaches = coaches.filter(COACHID__icontains=search_query)
    return render(request, 'coach/coach.html', {'coaches': coaches})

@login_required
def coach_create(request):
    if request.method == 'POST':
        form = CoachForm(request.POST, request.FILES)
        if form.is_valid():
            coach = form.save(commit=False)
            club = coach.CLUBID  # Lấy club từ coach
            if Coach.objects.filter(CLUBID=club).exists():
                messages.error(request, 'Đăng ký không thành công.')
            else:
                coach.owner = request.user  # Lưu người dùng hiện tại là chủ sở hữu
                coach.save()
                messages.success(request, 'Đăng ký thành công.')
                clubid = coach.CLUBID
                return redirect('view_club', club_id=str(clubid))
    else:
        form = CoachForm()
    return render(request, 'coach/create_coach.html', {'form': form})

def coach_list_view(request):
    coaches = Coach.objects.all()

    # Xử lý yêu cầu tìm kiếm
    search_query = request.GET.get('search')
    if search_query:
        coaches = coaches.filter(COACHID__icontains=search_query)

    return render(request, 'coach/coach_list.html', {'coaches': coaches})

def coach_reject(request):
    return render(request, 'coach/coach_reject.html')

@login_required
def coach_edit_view(request, coach_id):
    coach = get_object_or_404(Coach, COACHID=coach_id)
    
    # Kiểm tra xem người dùng hiện tại có phải là chủ sở hữu không
    if coach.owner != request.user:
        return redirect('coach_reject')
    
    if request.method == 'POST':
        form = CoachForm(request.POST, request.FILES, instance=coach)
        if form.is_valid():
            form.save()
            messages.success(request, 'Đã cập nhật thông tin huấn luyện viên.')
            clubid = coach.CLUBID
            return redirect('view_club', club_id=str(clubid))
    else:
        form = CoachForm(instance=coach)
    
    return render(request, 'coach/edit_coach.html', {'form': form})

@login_required
def coach_delete_view(request, coach_id):
    coach = get_object_or_404(Coach, COACHID=coach_id)
    clubid = coach.CLUBID
    # Kiểm tra xem người dùng hiện tại có phải là chủ sở hữu không
    if coach.owner != request.user:
        return redirect('coach_reject')
    
    if request.method == 'POST':
        coach.delete()
        messages.success(request, 'Đã xóa huấn luyện viên thành công.')
        return redirect('view_club', club_id=str(clubid))
    
    return render(request, 'coach/delete_coach.html', {'coach': coach})

@login_required
def toggle_follow_coach(request, coach_id):
    coach = get_object_or_404(Coach, pk=coach_id)
    user = request.user

    if user in coach.followers.all():
        coach.followers.remove(user)
    else:
        coach.followers.add(user)

    return redirect('coach')

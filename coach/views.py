# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from .forms import CoachForm
from .models import Coach

def coach_view(request):
    coaches = Coach.objects.all()
    return render(request, 'coach/coach.html', {'coaches': coaches})

@login_required
def coach_create(request):
    if request.method == 'POST':
        form = CoachForm(request.POST, request.FILES)
        if form.is_valid():
            coach = form.save(commit=False)
            coach.owner = request.user
            coach.save()
            messages.success(request, 'Đã thêm huấn luyện viên thành công.')
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
            return redirect('coach_list')
    else:
        form = CoachForm(instance=coach)
    
    return render(request, 'coach/edit_coach.html', {'form': form})

@login_required
def coach_delete_view(request, coach_id):
    coach = get_object_or_404(Coach, COACHID=coach_id)
    
    # Kiểm tra xem người dùng hiện tại có phải là chủ sở hữu không
    if coach.owner != request.user:
        return redirect('coach_reject')
    
    if request.method == 'POST':
        coach.delete()
        messages.success(request, 'Đã xóa huấn luyện viên thành công.')
        return redirect('coach_list')
    
    return render(request, 'coach/delete_coach.html', {'coach': coach})

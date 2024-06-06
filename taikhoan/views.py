from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponseRedirect
from .forms import RegistrationForm
from django.urls import reverse
from django.contrib import messages
from .forms import CustomPasswordChangeForm
from .forms import UserUpdateForm
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
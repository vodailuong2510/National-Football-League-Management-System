from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponseRedirect
from .forms import RegistrationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .forms import CustomPasswordChangeForm
# Create your views here.
# views.py

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'register.html', {'form' : form})

def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) 
            messages.success(request, 'Mật khẩu của bạn đã được thay đổi thành công!')
            return redirect('/') 
        else:
            messages.error(request, 'Vui lòng kiểm tra lại thông tin.')
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})
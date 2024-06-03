from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.utils.html import format_html

def nbsp(times):
    return format_html('&nbsp;' * times)

class RegistrationForm(forms.Form):
    username = forms.CharField(label=format_html('Tên tài khoản{}', nbsp(8)), max_length=10, widget=forms.TextInput(attrs={'placeholder': 'Số điện thoại'}))
    password1 = forms.CharField(label=format_html('Mật khẩu{}', nbsp(15)), widget=forms.PasswordInput(attrs={'placeholder': 'Mật khẩu'}))
    password2 = forms.CharField(label='Nhập lại mật khẩu', widget=forms.PasswordInput(attrs={'placeholder': 'Nhập lại mật khẩu'}))
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 == password2 and password1:
            return password2
        else:
            raise forms.ValidationError('Mật khẩu không khớp')
    def clean_username(self):
        username = self.cleaned_data['username']
        if not username.isdigit():
            raise forms.ValidationError('Tên tài khoản phải là số điện thoại')
        if len(username) != 10: 
            raise forms.ValidationError('Tên tài khoản phải có đúng 10 chữ số')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('Tài khoản đã tồn tại')
    
    def save(self):
        User.objects.create_user(username = self.cleaned_data['username'], password=self.cleaned_data['password2'])

from django import forms
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
        
        if password1 and len(password1) < 8:
            raise forms.ValidationError('Mật khẩu phải có ít nhất 8 ký tự')
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Mật khẩu không khớp')
        
        return password2
        
    def clean_username(self):
        username = self.cleaned_data['username']
        if not username.isdigit() or username[0] != '0':
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

from django.contrib.auth.forms import PasswordChangeForm

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=format_html('Mật khẩu cũ{}', nbsp(18)),
        widget=forms.PasswordInput(attrs={'placeholder': 'Mật khẩu cũ'}),
    )
    new_password1 = forms.CharField(
        label=format_html('Mật khẩu mới{}', nbsp(16)),
        widget=forms.PasswordInput(attrs={'placeholder': 'Mật khẩu mới'}),
    )
    new_password2 = forms.CharField(
        label='Nhập lại mật khẩu mới',
        widget=forms.PasswordInput(attrs={'placeholder': 'Mật khẩu mới'}),
    )
class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(required=False)
    class Meta:
        model = User
        fields = [ 'username','first_name',  'email', 'date_joined']

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['username'].disabled = True
        self.fields['username'].label = format_html('Tên tài khoản{}', nbsp(8))

        self.fields['date_joined'].disabled = True
        self.fields['date_joined'].label = format_html('Ngày tham gia{}', nbsp(8))

        self.fields['email'].widget.attrs.update({'style': 'width: 190px; height: 35px'})
        self.fields['email'].label = format_html('Email{}', nbsp(23))

        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['first_name'].label = format_html('Họ và tên{}', nbsp(16))


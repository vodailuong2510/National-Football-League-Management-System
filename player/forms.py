from django import forms
from .models import Player

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['PLAYERID', 'PLAYERNAME', 'BIRTHDAY', 'NATIONALITY','CLUBID', 'IMAGE', 'POSITION', 'SHIRTNUM', 'HEIGHT', 'WEIGHT', 'PREFERFOOT']

    def __init__(self, *args, **kwargs):
        disable_playerid = kwargs.pop('disable_playerid', False)
        super(PlayerForm, self).__init__(*args, **kwargs)
        
        self.fields['PLAYERID'].widget.attrs.update({'class': 'form-control', 'placeholder': 'ID cầu thủ'})
        self.fields['PLAYERNAME'].widget.attrs.update({'class': 'my-input', 'placeholder': 'Tên cầu thủ'})
        self.fields['BIRTHDAY'].widget.attrs.update({'class': 'my-input', 'placeholder': 'dd/mm/YYYY'})
        self.fields['NATIONALITY'].widget.attrs.update({'class': 'my-input', 'placeholder': 'Quốc tịch'})
        self.fields['CLUBID'].widget.attrs.update({'class': 'my-input', 'placeholder': 'Đội bóng'})
        self.fields['IMAGE'].widget.attrs.update({'class': 'my-input', 'placeholder': 'Ảnh'})
        self.fields['POSITION'].widget.attrs.update({'class': 'my-input', 'placeholder': 'Vị trí'})
        self.fields['SHIRTNUM'].widget.attrs.update({'class': 'my-input', 'placeholder': 'Số áo'})
        self.fields['HEIGHT'].widget.attrs.update({'class': 'my-input', 'placeholder': 'Chiều cao'})
        self.fields['WEIGHT'].widget.attrs.update({'class': 'my-input', 'placeholder': 'Cân nặng'})
        self.fields['PREFERFOOT'].widget.attrs.update({'class': 'my-input', 'placeholder': 'Chân thuận'})
        
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': 'my-input'})
                
        if disable_playerid:
            self.fields['PLAYERID'].disabled = True
                
    def clean_PLAYERID(self):
        PLAYERID = self.cleaned_data.get('PLAYERID')
        if Player.objects.filter(PLAYERID=PLAYERID).exists():
            raise forms.ValidationError('ID already exists')
        return PLAYERID

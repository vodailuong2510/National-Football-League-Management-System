from django import forms
from .models import Club
from datetime import datetime

class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = [
            'CLUBID', 'CLUBNAME', 'LOGO', 'FOUNDED', 'EMAIL', 'PHONE', 
            'COACH', 'CAPTAIN', 'STADIUM', 'CAPACITY', 'TOTALPLAYERS', 'LEAGUEPLAYING'
        ]
    def __init__(self, *args, **kwargs):
        super(ClubForm, self).__init__(*args, **kwargs)
        self.fields['CLUBID'].widget.attrs.update({'class': 'form-control'})
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': 'my-input'})
            
    def clean_FOUNDED(self):
        founded = self.cleaned_data.get('FOUNDED')
        if founded:
            try:
                # Kiểm tra ngày tháng có hợp lệ không
                datetime.strptime(founded.strftime('%Y-%m-%d'), '%Y-%m-%d')
            except ValueError:
                raise forms.ValidationError("Invalid date.")

            # Kiểm tra năm nhuận
            year = founded.year
            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0:
                        is_leap = True
                    else:
                        is_leap = False
                else:
                    is_leap = True
            else:
                is_leap = False

            if not is_leap and founded.month == 2 and founded.day == 29:
                raise forms.ValidationError("Invalid date.")

        return founded

    def clean_CAPACITY(self):
        capacity = self.cleaned_data.get('CAPACITY')
        if capacity < 1000:
            raise forms.ValidationError("Sức chứa tối thiểu là 1000.")
        return capacity

    def clean_TOTALPLAYERS(self):
        total_players = self.cleaned_data.get('TOTALPLAYERS')
        if total_players < 16:
            raise forms.ValidationError("Yêu cầu đội bóng phải có tối thiểu 16 cầu thủ.")
        return total_players
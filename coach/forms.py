from django import forms
from .models import Coach

class CoachForm(forms.ModelForm):
    class Meta:
        model = Coach
        fields = ['COACHID', 'COACHNAME', 'BIRTHDAY', 'NATIONALITY', 'CLUBID', 'IMAGE']
    
    def __init__(self, *args, **kwargs):
        disable_coachid = kwargs.pop('disable_coachid', False)
        super(CoachForm, self).__init__(*args, **kwargs)
        
        self.fields['COACHID'].widget.attrs.update({'class': 'form-control', 'placeholder': 'ID HLV'})
        self.fields['COACHNAME'].widget.attrs.update({'class': 'my-input', 'placeholder': 'Tên HLV'})
        self.fields['BIRTHDAY'].widget.attrs.update({'class': 'my-input', 'placeholder': 'dd/mm/YYYY'})
        self.fields['NATIONALITY'].widget.attrs.update({'class': 'my-input', 'placeholder': 'Quốc tịch'})
        self.fields['CLUBID'].widget.attrs.update({'class': 'my-input', 'placeholder': 'Đội bóng'})
        self.fields['IMAGE'].widget.attrs.update({'class': 'my-input', 'placeholder': 'Ảnh'})         
                
        if disable_coachid:
            self.fields['COACHID'].disabled = True
                
    def check_id(self, COACHID):
        if Coach.objects.filter(COACHID=COACHID).exists():
            raise forms.ValidationError('ID already exists')
        return COACHID

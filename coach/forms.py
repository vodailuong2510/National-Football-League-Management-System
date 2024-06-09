from django import forms
from .models import Coach

class CoachForm(forms.ModelForm):
    class Meta:
        model = Coach
        fields = ['COACHID', 'COACHNAME', 'BIRTHDAY', 'NATIONALITY', 'CLUB', 'IMAGE', 'CARDS']
    
    def __init__(self, *args, **kwargs):
        super(CoachForm, self).__init__(*args, **kwargs)
        self.fields['COACHID'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Mã HLV'})
from django import forms
from .models import Stats
#needs editing

class MyForm(forms.ModelForm):
    class Meta:
        model = Stats
        fields = ['current_rent']
        widgets = {'current_rent': forms.Select}





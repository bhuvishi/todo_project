from django import forms
from .models import SingleTODO

class SingleTODOForm(forms.ModelForm):
    class Meta:
        model = SingleTODO
        fields = ['title']
from django import forms
from .models import *

class details(forms.ModelForm):
    class Meta:
        model=order
        fields='__all__'
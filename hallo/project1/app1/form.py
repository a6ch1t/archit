from django import forms
from .models import *

class detailsee(forms.ModelForm):
    class Meta:
        model=Order
        fields='__all__'
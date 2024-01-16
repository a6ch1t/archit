from django import forms
from .models import *

class ryde(forms.ModelForm):
    class Meta:
        model=eeko
        fields='__all__'
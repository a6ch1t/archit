from django import forms
from .models import *

from app1.models import *

class ryde(forms.ModelForm):
    class Meta:
        model=eeeko
        fields='__all__'
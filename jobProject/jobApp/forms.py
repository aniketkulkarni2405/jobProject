from django import forms
from jobApp.models import *
class createForm(forms.ModelForm):
    class Meta:
        model=Chennaijobs
        fields='__all__'

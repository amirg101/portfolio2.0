from .models import *
from .views import *
from django import forms
from django.forms import ModelForm
class contactForm(forms.ModelForm):
    class Meta:
        model=getInTouch
        fields='__all__'

        widget={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'subject':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'message':forms.TextInput(attrs={'class':'form-control'}),
           
        }

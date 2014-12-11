# -*- coding: utf-8 -*-
from django import forms
#from polls.models import UserInput
from .models import UserInput
from django.forms import ModelForm, Textarea



# it works
class UserInputForm(forms.Form):
    form_translation = forms.CharField(widget=forms.Textarea(attrs={'cols':25, 'rows':4}), label='', required=True)
      
    class Meta: 
        model = UserInput


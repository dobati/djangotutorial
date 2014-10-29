from django import forms
from polls.models import UserInput

class UserInputForm(forms.ModelForm):
    class Meta:
        model = UserInput

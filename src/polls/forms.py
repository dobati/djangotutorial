from django import forms
from polls.models import UserInput
from django.forms import ModelForm, Textarea

# it works
class UserInputForm(forms.Form):
    form_translation = forms.CharField(widget=forms.Textarea, label='', required=True)
    
    
    #class Meta: 
     #   model = UserInput




# 1. class MyForm(forms.Form):
#     myfield = forms.CharField(widget=forms.TextInput(attrs={'class' : 'myfieldclass'}))

# 2. add the class = myfielfclass to your form taf with method = post
# 3. add the desirable window styling from http://html-generator.weebly.com/css-textbox-style.html
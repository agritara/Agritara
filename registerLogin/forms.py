from django import forms
from django.forms import ModelForm
from registerLogin.models import RegisterLogin
from registerLogin.models import RegisterLogin

class RegisLogForm(ModelForm):
   
    class Meta:
        model = RegisterLogin
        fields = ('username', 'user_type','provinsi','password')
    

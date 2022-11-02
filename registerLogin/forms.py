from django import forms
from django.forms import ModelForm
from registerLogin.models import RegisterLogin
from registerLogin.models import RegisterLogin

<<<<<<< HEAD
class RegisLogForm( ModelForm):
    class Meta:
        model = RegisterLogin
        fields = ('username', 'user_type','provinsi','password')
=======
class RegisLogForm(ModelForm):
   
    class Meta:
        model = RegisterLogin
        fields = ('username', 'user_type','provinsi','password')
    
>>>>>>> a385b0af88aee3d16c309c7abbad69dbed9c42b8

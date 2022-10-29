from django import forms
from django.forms import ModelForm
from register_login.models import register_login
from register_login.models import register_login

class TaskForm(ModelForm):
    class Meta:
        model = register_login
        fields = ('title', 'description')
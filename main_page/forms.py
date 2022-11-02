from django import forms
from main_page.models import FeedBack
from django.forms import ModelForm

class FeedbackForm(ModelForm):
    class Meta:
        model = FeedBack
        fields = [
            'feedback'
        ]

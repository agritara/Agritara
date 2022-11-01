# from https://www.youtube.com/watch?v=EX6Tt-ZW0so

from django.forms import ModelForm
from .models import OrderHistory

class PurchaseHistoryForm(ModelForm):
    class Meta:
        model = OrderHistory
        fields = ['review']
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class OrderHistory(models.Model):
    purchased_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    item = models.CharField(max_length=50)
    item_amount = models.IntegerField(default=0)
    closed_date = models.DateField(auto_now_add=True, null=True)
    review = models.TextField(default='')

from email.policy import default
from django.db import models

# Create your models here.
class OrderHistory(models.Model):
    # purchased_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    item = models.CharField(max_length=50)
    item_amount = models.IntegerField(default=0)
    closed_date = models.DateField(auto_now_add=True, null=True)
<<<<<<< HEAD
    review = models.TextField(default='0000000')
=======
    review = models.TextField(default='')
>>>>>>> fcc9f8b6eb5b6a287ddd687b3be92e406887e704

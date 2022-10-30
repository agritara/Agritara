from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class GovReqItem(models.Model):
    # user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    request = models.CharField(max_length=50)
    kuantitas_req = models.BigIntegerField()
    request_date = models.DateField(auto_now_add=True, null=True)
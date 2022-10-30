from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class GovReqItem(models.Model):
    request = models.TextField()
    kuantitas_req = models.BigIntegerField()
     
    



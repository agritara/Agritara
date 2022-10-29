from django.db import models
from django.contrib.auth.models import User

class RegisterLogin(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default='')
    user_type = models.DateField()
    password = models.CharField(max_length=30)
    


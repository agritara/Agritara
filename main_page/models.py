from django.db import models

# Create your models here.
class FeedBack(models.Model):
    feedback = models.TextField()

class Rate(models.Model):
    numRate = models.IntegerField()
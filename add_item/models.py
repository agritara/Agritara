from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class BarangPetani(models.Model):
    nama_barang = models.CharField(max_length=255)
    kuantitas_barang = models.BigIntegerField()
    daerah_asal = models.CharField(max_length=255, default = "Jakarta")
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
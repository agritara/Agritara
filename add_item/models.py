from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class BarangPetani(models.Model):
    nama_barang = models.CharField(max_length=255)
    kuantitas_barang = models.BigIntegerField()
    daerah_asal = models.CharField(max_length=255, default = "Jakarta")
    # pengguna = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    date = models.DateField(default=timezone.now)
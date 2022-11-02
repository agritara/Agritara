from django.db import models
from django.contrib.auth.models import User

TIPE_USER = (
    ('petani','PETANI'),
    ('pemda','PEMDA'),
)
PROVINSI =(
    ('Aceh','ACEH'),
    ('Sumatra Utara','SUMATRA UTARA'),
    ('Sumatra Barat','SUMATRA BARAT'),
    ('Riau','RIAU'),
    ('Kepulauan Seribu','KEPULAUAN RIAU'),
    ('Jambi','JAMBI'),
    ('Bengkulu','BENGKULU'),
    ('Sumatra Selatan','SUMATRA SELATAN'),
    ('Kepulauan Bangka Belitung','KEPULAUAN BANGKA BELITUNG'),
    ('Lampung','LAMPUNG'),
    ('Banten','BANTEN'),
    ('DKI Jakarta','DKI JAKARTA'),
    ('Jawa Barat','JAWA BARAT'),
    ('Jawa Tengah','JAWA TENGAH'),
    ('Daerah Istimewa Yogyakarta','DAERAH ISTIMEWA YOGYAKARTA'),
    ('Jawa Timur','JAWA TIMUR'),
    ('Bali','BALI'),
    ('Nusa Tenggara Barat','NUSA TENGGARA BARAT'),
    ('Nusa Tenggara Timur','NUSA TENGGARA TIMUR'),
    ('Kalimantan Barat','KALIMANTAN BARAT'),
    ('Kalimantan Tengah','KALIMANTAN TENGAH'),
    ('Kalimantan Selatan','KALIMANTAN SELATAN'),
    ('Kalimantan Timur','KALIMANTAN TIMUR'),
    ('Kalimantan Utara','KALIMANTAN UTARA'),
    ('Sulawesi Barat','SULAWESI BARAT'),
    ('Sulawesi Selatan','SULAWESI SELATAN'),
    ('Sulawesi Tenggara','SULAWESI TENGGARA'),
    ('Sulawesi Tengah','SULAWESI TENGAH'),
    ('Gorontalo','GORONTALO'),
    ('Sulawesi Utara','SULAWESI UTARA'),
    ('Maluku Utara','MALUKU UTARA'),
    ('Maluku','MALUKU'),
    ('Papua','PAPUA'),
    ('Papua Tengah','PAPUA TENGAH'),
    ('Papua Pegunungan','PAPUA PEGUNUNGAN'),
    ('Papua Selatan','PAPUA SELATAN'),
)
class RegisterLogin(models.Model):
    user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    user_type = models.CharField(max_length=6, choices=TIPE_USER, default='petani')
    provinsi = models.CharField(max_length=38, choices=PROVINSI, default='Aceh')

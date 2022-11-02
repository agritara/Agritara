from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from registerLogin.models import RegisterLogin

TIPE_USER = [
    ('petani','PETANI'),
    ('pemda','PEMDA'),
]
PROVINSI = [
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
]

class RegisLogForm( UserCreationForm):
    user_type = forms.CharField(label="user type",widget = forms.Select(choices=TIPE_USER))
    provinsi = forms.CharField(label="provinsi",widget =  forms.Select(choices=PROVINSI))
    class Meta:
        model = User
        fields = ['username','password']

from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from registerLogin.models import RegisterLogin
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from registerLogin.forms import RegisLogForm


def register(request):
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
    form = RegisLogForm()

    if request.method == "POST":
        form = RegisLogForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            data_register_login = RegisterLogin.objects.all()
            for user in data_register_login:
                return redirect('pemda_home:login')
    

    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("registerLogin:registerlogin"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    
        else:
            messages.info(request, 'Username atau Password salah!')

    context = {}
    return render(request, 'login.html', context)

@login_required(login_url='/regsiterLogin/login/')
def show_registerlogin(request):
    data_register_login = RegisterLogin.objects.all()
    context = {
    'list_registerlogin': data_register_login,
    'nama': 'Kak Cinoy',
    'last_login': request.COOKIES['last_login'],
}
    return render(request, "login.html")

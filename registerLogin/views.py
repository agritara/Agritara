import json
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from registerLogin.models import RegisterLogin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from registerLogin.forms import RegisLogForm
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def register(request):
    form = RegisLogForm()
    if request.method == "POST":
        form = RegisLogForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')    
            print("berhasil")
            return redirect('registerLogin:login')
    

    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request): 
    print("berhasil")
    if request.method == 'POST':
        print("masuk")
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("check")
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect("") # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) 
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    return render(request,'login.html')

@login_required(login_url='/registerLogin/login/')
def show_registerlogin(request):
    data_register_login = RegisterLogin.objects.all()
    context = {
    'list_registerlogin': data_register_login,
    'last_login': request.COOKIES['last_login'],
}
    return render(request, "baru.html")


@csrf_exempt
def login_flutter(request):
     username = request.POST['username']
     password = request.POST['password']
     user = authenticate(username=username, password=password)
     if user is not None:
         if user.is_active:
             auth_login(request, user)
             # Redirect to a success page.
             return JsonResponse({
               "status": True,
               "message": "Successfully Logged In!"
               # Insert any extra data if you want to pass data to Flutter
             }, status=200)
         else:
             return JsonResponse({
               "status": False,
               "message": "Failed to Login, Account Disabled."
             }, status=401)

     else:
         return JsonResponse({
           "status": False,
           "message": "Failed to Login, check your email/password."
         }, status=401)

def register_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        username = data["username"]
        email = data["email"]
        password1 = data["password1"]

        newUser = RegisterLogin.objects.create_user(
        username = username, 
        email = email,
        password = password1,
        )

        newUser.save()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
def logoutFlutter(request):
    try:
        logout(request)
        return JsonResponse({
                    "status": True,
                    "message": "Successfully Logged out!"
                }, status=200)
    except:
        return JsonResponse({
          "status": False,
          "message": "Failed to Logout"
        }, status=401)
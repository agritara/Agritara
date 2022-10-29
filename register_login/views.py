from django.shortcuts import render
from register_login.models import RegisterLogin, register_login

from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from register_login.forms import TaskForm
from register_login.models import register_login

@login_required(login_url='/register_login/login/')
def show_register_login(request):
    data_register_login = RegisterLogin.objects.all()
    context = {
        'list_user': data_register_login,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "register_login.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('register_login:login')

    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("register_login:show_register_login"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('register_login:login'))
    response.delete_cookie('last_login')
    return response

def task_user(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            task = register_login()
            task.user = request.user
            task.user_type = datetime.datetime.now()
            task.title = form.cleaned_data['title']
            task.description = form.cleaned_data['description']
            task.save()
            messages.success(request, 'Task telah berhasil dibuat!')
            return HttpResponseRedirect(reverse('register_login:show_register_login'))

    return render(request, 'create-task.html', {'form': form})
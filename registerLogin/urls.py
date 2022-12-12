from django.urls import path
from registerLogin.views import show_registerlogin
from registerLogin.views import register 
from registerLogin.views import login_user 
from registerLogin.views import login_flutter
from registerLogin.views import register_flutter
from registerLogin.views import logout_Flutter


app_name = 'registerLogin'

urlpatterns = [
    path('', show_registerlogin, name='show_registerlogin'),
    path('register/', register, name='register'), 
    path('login/', login_user, name='login'), 
    path('login_flutter/', login_flutter, name='login_flutter'),
    path('register_flutter/', register_flutter, name='register_flutter'),
    path('logout_flutter', logout_Flutter, name='logout_flutter'),
]
from django.urls import path
from register_login.views import show_register_login
from register_login.views import login_user 
from register_login.views import logout_user
from register_login.views import register


app_name = 'register_login'

urlpatterns = [
    path('', show_register_login, name='show_register_login'),
    path('', show_register_login, name='show_register_login'), 
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
    
]
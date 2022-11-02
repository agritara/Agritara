from django.urls import path
from .views import load_page, load_history, logout_user

urlpatterns = [
    path('home/', load_page, name='load_page'),
    path('history/', load_history, name='load_history'),
    path('logout/', logout_user, name='logout'),
]

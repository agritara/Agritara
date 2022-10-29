from django.urls import path
from .views import load_page, load_history

urlpatterns = [
    path('', load_page, name='load_page'),
    path('history/', load_history, name='load_history'),
]

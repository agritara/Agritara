from django.urls import path
from .views import load_page

urlpatterns = [
    path('home/', load_page, name='load_page'),
]

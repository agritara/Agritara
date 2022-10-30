from django.urls import path
from .views import index, show_as_json, show_barang_petani

urlpatterns = [
    path('json/', show_as_json, name='show_as_json'),
    path('', show_barang_petani, name='show_barang_petani')
]
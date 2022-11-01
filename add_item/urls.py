from django.urls import path

from add_item.views import index, get_barang_petani_json, add_barang_petani

urlpatterns = [
    path('', index, name='index'),
    path('get_barang/', get_barang_petani_json, name='get_barang_petani_json'),
    path('nambah_barang/', add_barang_petani, name='add_barang_petani'),
]
from django.urls import path
from add_item.views import add_wishlist_item, get_wishlist_json, wishlist
from add_item.views import index, get_barang_petani_json, add_barang_petani

urlpatterns = [
    path('', wishlist, name='wishlist'),
    path('get_data/', get_wishlist_json, name='get_wishlist_json'),
    path('create_data/', add_wishlist_item, name='add_wishlist_item'),
    path('index/', index, name='index'),
    path('get_barang/', get_barang_petani_json, name='get_barang_petani_json'),
    path('nambah_barang/', add_barang_petani, name='add_barang_petani'),
]
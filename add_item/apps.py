from django.apps import AppConfig


class AddItemConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'add_item'

class BarangWishlistConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'barang_wishlist'

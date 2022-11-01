from django.shortcuts import render

from add_item.models import BarangWishlist, BarangPetani

from django.http import HttpResponse, HttpResponseNotFound


from django.core import serializers

# Create your views here.
def wishlist(request):
    return render(request, "index_wishlist.html")

def get_wishlist_json(request):
    wishlist_item = BarangWishlist.objects.all()
    return HttpResponse(serializers.serialize('json', wishlist_item))

def add_wishlist_item(request):
    if request.method == 'POST':
        nama_barang = request.POST.get("nama_barang")
        harga_barang = request.POST.get("harga_barang")
        deskripsi = request.POST.get("deskripsi")

        new_barang = BarangWishlist(nama_barang=nama_barang, harga_barang=harga_barang, deskripsi=deskripsi)
        new_barang.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def index(request):
    return render(request, 'add.html')

def get_barang_petani_json(request):
    barang_petani = BarangPetani.objects.all()
    return HttpResponse(serializers.serialize('json', barang_petani))

def add_barang_petani(request):
    if request.method == 'POST':
        nama_barang = request.POST.get("nama_barang")
        kuantitas_barang = request.POST.get("kuantitas_barang")

        # new_barang = BarangPetani(nama_barang = nama_barang, kuantitas_barang = kuantitas_barang, user = request.user)
        new_barang = BarangPetani(nama_barang = nama_barang, kuantitas_barang = kuantitas_barang)
        new_barang.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()



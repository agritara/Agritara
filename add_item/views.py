from django.shortcuts import render

from add_item.models import BarangPetani

from django.http import HttpResponse, HttpResponseNotFound

from django.core import serializers

# from django.contrib.auth.decorators import login_required

# import datetime
# from django.http import HttpResponseRedirect
# from django.urls import reverse

# @login_required(login_url='/registerLogin/login/')
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



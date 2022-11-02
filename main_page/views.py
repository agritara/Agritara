from django.shortcuts import render
from add_item.models import BarangPetani
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from main_page.forms import FeedbackForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
import json
from main_page.models import FeedBack

class Comm_Prov():
    prov = ""
    comm = ""
    quantity = 0

def main(request):
    barang_petani = BarangPetani.objects.all()
    data_provinsi = {
        "Jakarta" : 0,
        "Jawa Barat" : 0,
        "Banten" : 0,
        "Jawa Tengah" : 0,
        "Daerah Istimewa Yogyakarta" : 0,
        "Jawa Timur" : 0,
        "Bali" : 0,
        "Nusa Tenggara Barat" : 0,
        "Nusa Tenggara Timur" : 0,
        "Sulawesi Utara" : 0,
        "Sulawesi Barat" : 0,
        "Sulawesi Tengah" : 0,
        "Sulawesi Tenggara" : 0,
        "Sulawesi Selatan" : 0,
        "Gorontalo" : 0,
        "Naggroe Aceh Darussalam" : 0,
        "Sumatra Utara" : 0,
        "Sumatera Barat" : 0,
        "Riau" : 0,
        "Kepulauan Riau" : 0,
        "Jambi" : 0,
        "Sumatra Selatan" : 0,
        "Bangka Belitung" : 0,
        "Bengkulu" : 0,
        "Lampung" : 0,
        "Kalimantan Utara" : 0,
        "Kalimantan Barat" : 0,
        "Kalimantan Tengah" : 0,
        "Kalimantan Selatan" : 0,
        "Kalimantan Timur" : 0,
        "Maluku" : 0,
        "Maluku Utara" : 0,
        "Papua Barat" : 0,
        "Papua" : 0,
        "Papua Selatan" : 0,
        "Papua Tengah" : 0,
        "Papua Pegunungan" : 0
    }

    data_komoditas = {}
    data_komoditas_per_provinsi = {}
    for input in barang_petani:
        data_provinsi[input.daerah_asal] += input.kuantitas_barang
        data_komoditas[input.nama_barang] = 0
        data_komoditas_per_provinsi[str(input.daerah_asal+" "+input.nama_barang)] = 0

    for komoditas in barang_petani:
        data_komoditas[komoditas.nama_barang] += komoditas.kuantitas_barang

    komod_per_prov= []

    for prov in data_provinsi.keys():
        for komo in barang_petani:
            if str(prov+" "+komo.nama_barang) in data_komoditas_per_provinsi.keys():
                data_komoditas_per_provinsi[str(prov+" "+komo.nama_barang)] += komo.kuantitas_barang
    
    for string in data_komoditas_per_provinsi.keys():
        tempobj = Comm_Prov()
        tempobj.prov = string.split(" ")[0]
        tempobj.comm = " ".join(string.split(" ")[1:])
        tempobj.quantity = data_komoditas_per_provinsi[string]
        komod_per_prov.append(tempobj)        

    context = {
        'list_masukan_petani' : barang_petani,
        'list_komod_per_prov' : komod_per_prov,
        'list_provinsi' : data_provinsi,
        'list_komoditas' : data_komoditas
    }
    return render(request, 'main_page.html', context)

def add_feedback(request):
    form = FeedbackForm()

    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # form = form.save(commit=False)
            feedback = request.POST.get("feedback")
            new_feedback = FeedBack(feedback = feedback)
            new_feedback.save()
            messages.success(request, 'Berhasil membuat task!')
            return redirect('main_page')

    context = {'form': form}
    return render(request, 'add_feedback.html', context)

# def add_feedback(request):
#     if request.method == 'POST':
#         feedback = request.POST.get("feedback")

#         new_feedback = FeedBack(feedback=feedback)
#         new_feedback.save()

#         return HttpResponse(b"CREATED", status=201)
#     return HttpResponseNotFound()

def post_ajax_feedback(request):
    print("ayyayay")
    if request.method == 'POST':
        feedback = request.POST['feedback']

        ins = FeedBack(feedback=feedback)
        ins.save()

        data = {
            "message" : 'Submitted!'
        }
        json_obj = json.dumps(data, indent = 4)
        return JsonResponse(json.loads(json_obj))
    return render(request, "add_feedback.html")

def show_feedback_ajax(request):
    feedbacks = FeedBack.objects.all()
    context = {
    'list_feedbacks': feedbacks,
    }
    return render(request, "main_page.html", context)

def get_feedback_json(request):
    feedback_item = FeedBack.objects.all()
    return HttpResponse(serializers.serialize('json', feedback_item))

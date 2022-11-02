from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from .models import OrderHistory
from .forms import PurchaseHistoryForm
from req_item.models import GovReqItem
from add_item.models import BarangPetani

# Create your views here.
def load_page(request):
    if request.method == "POST":
        # uid = request.user.id
        item_id = request.POST.get('item_id')
        # print(item_id)
        govitem = get_object_or_404(GovReqItem, id=item_id)
        # print(item.request)
        govitem_name = govitem.request

        petaniitem = get_object_or_404(BarangPetani, nama_barang=govitem_name)

        govitem_amount = govitem.kuantitas_req
        review = request.POST.get('review')

        if review == "" or review == None:
            review = '-'

        OrderHistory.objects.create(item=govitem_name, item_amount=govitem_amount, review=review)
        new_qty = petaniitem.kuantitas_barang - govitem_amount
        if new_qty>0:
            BarangPetani.object.create(nama_barang=govitem_name, kuantitas_barang=new_qty, daerah_asal=petaniitem.daerah_asal, date=petaniitem.date)

        petaniitem.delete()
        govitem.delete()

    return render(request, 'pemda_home.html')

def load_history(request):
    data = OrderHistory.objects.all() #filter(user=request.user.id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
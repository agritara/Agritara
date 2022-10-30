from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from .models import OrderHistory
from .forms import PurchaseHistoryForm
from req_item.models import GovReqItem

# Create your views here.
def load_page(request):
    if request.method == "POST":
        # uid = request.user.id
        item_id = request.POST.get('item_id')
        print(item_id)
        item = get_object_or_404(GovReqItem, id=item_id)
        print(item.request)
        item_name = item.request
        item_amount = item.kuantitas_req
        review = request.POST.get('review')
        OrderHistory.objects.create(item=item_name, item_amount=item_amount, review=review)

        item.delete()

    return render(request, 'pemda_home.html')

def load_history(request):
    data = OrderHistory.objects.all() #filter(user=request.user.id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
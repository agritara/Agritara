from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from .models import OrderHistory
from .forms import PurchaseHistoryForm

# Create your views here.
def load_page(request):
    if request.method == "POST":
        # uid = request.user.id
        item=request.POST.get('item')
        print(item)
        item_amount=0
        review = request.POST.get('review')
        # OrderHistory.objects.create(item=item, item_amount=item_amount, review=review)

    return render(request, 'pemda_home.html')

def load_history(request):
    data = OrderHistory.objects.all() #filter(user=request.user.id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
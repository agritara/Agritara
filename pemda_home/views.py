from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import OrderHistory

# Create your views here.
def load_page(request):
    return render(request, 'pemda_home.html')

def load_history(request):
    data = OrderHistory.objects.all() #filter(user=request.user.id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def load_history_search(request):
    
    # data = OrderHistory.objects.filter()
    return None
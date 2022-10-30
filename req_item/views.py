from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from req_item.forms import request_form
from req_item.models import GovReqItem
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm

def governments_request_page(request):
    Gov_request = GovReqItem.objects.all()
    context = {
        'list_request':Gov_request,
    }
    response = {'Gov_request':Gov_request}
    return render(request, 'government_request_page.html', context, response)

def add_governments_request(request):
    form_request = request_form() 
    if request.method == "POST":
        form_request= request_form(request.POST or None, request.FILES or None)
        if form_request.is_valid():
            req_pemerintah = GovReqItem()
            req_pemerintah.request = form_request.cleaned_data['request']
            req_pemerintah.kuantitas_req = form_request.cleaned_data['kuantitas_req']
            request = form_request.save(commit=False)
            request.save()
            response = HttpResponseRedirect(reverse("req_item:governments_request_page"))
            return response

    context = {'form_request':form_request,
    'title':"Tambah Request", 
    }
    return render(request, 'government_request_page.html', context)


    
    








    
    





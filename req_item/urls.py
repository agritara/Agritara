from operator import add
from django.urls import path
from req_item.views import add_governments_request

app_name = 'req_item'

urlpatterns = [
    path('request/', add_governments_request, name='add_government_request'),
]
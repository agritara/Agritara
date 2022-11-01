from django import forms
from req_item.models import GovReqItem

class request_form(forms.ModelForm):
    class Meta:
        model = GovReqItem
        fields = {"request", "kuantitas_req"}
        widgets = {
            "request" : forms.TextInput(attrs={"class":"form-control"}),
            "kuantitas_req" : forms.TextInput(attrs={"class":"form-control"}), 
        }
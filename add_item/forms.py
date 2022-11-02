from django import forms
from add_item.models import BarangPetani

class request_form(forms.ModelForm):
    class Meta:
        model = BarangPetani
        fields = {"nama", "kuantitas"}
        widgets = {
            "nama" : forms.TextInput(attrs={"class":"form-control"}),
            "kuantitas" : forms.TextInput(attrs={"class":"form-control"}), 
        }
from django import forms
from .models import AddPlace

class EditplaceForm(forms.ModelForm):
    class Meta:
        model=AddPlace
        fields=("name","addr",'open_time',"close_time")

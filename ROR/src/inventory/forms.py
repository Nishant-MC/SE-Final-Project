from django import forms

from .models import Item

class AddInventoryForm(forms.ModelForm):
    class Meta:
        model = Item
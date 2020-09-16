from django import forms
from .models import Item

# form to add item
class ItemForm(forms.ModelForm):
  class Meta:
    model = Item
    fields = ["item_name", "completed"]
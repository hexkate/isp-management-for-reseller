from django.forms import ModelForm
from .models import Product

# -------------------------------------------------#
# Warehouse product model form
# -------------------------------------------------#


class WarehouseProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'quantity', 'price', 'serial', 'status']

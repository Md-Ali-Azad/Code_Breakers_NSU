from django import forms 
from .models import Product_Price

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product_Price
        exclude = ('user',)
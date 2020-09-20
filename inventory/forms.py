from django import forms 
from .models import Product,Order,Delivery 

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('user',)
        

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('status','user')
        

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        exclude = ('user',)
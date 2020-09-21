from django import forms 
from .models import Product,Order,Delivery 
from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('user',)

class OrderForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super (OrderForm,self ).__init__(*args,**kwargs)
        user=get_current_user()
        self.fields['product'].queryset = Product.objects.filter(user=user)
        
    class Meta:
        model = Order
        exclude = ('status','user')
        

class DeliveryForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super (DeliveryForm,self ).__init__(*args,**kwargs)
        user=get_current_user()
        self.fields['order'].queryset = Order.objects.filter(user=user)
    class Meta:
        model = Delivery
        exclude = ('user',)
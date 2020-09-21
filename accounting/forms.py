from django import forms 
from .models import Completed_Order,Bill,Payment

class complete_order_form(forms.ModelForm):
    class Meta:
        model = Completed_Order
        exclude = ('user',)

class bill_form(forms.ModelForm):
    class Meta:
        model = Bill
        exclude = ('user',)

class payment_form(forms.ModelForm):
    class Meta:
        model = Payment
        exclude = ('user',)
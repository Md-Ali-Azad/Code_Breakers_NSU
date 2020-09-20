from django import forms 
from .models import Sales_Manager,Order_Status 
  
 
class OrderForm(forms.ModelForm): 
    class Meta: 
        model = Sales_Manager
        exclude = ('deliverd','user')

class OrderStatusForm(forms.ModelForm): 
    class Meta: 
        model = Order_Status
        exclude = ('user',)
  
class EmailForm(forms.Form): 
    description = forms.CharField(widget = forms.Textarea) 
    
from django import forms 
from .models import Sales_Manager,Order_Status 
from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)
 
class OrderForm(forms.ModelForm): 
    class Meta: 
        model = Sales_Manager
        exclude = ('deliverd','user')

class OrderStatusForm(forms.ModelForm): 
    def __init__(self,*args,**kwargs):
        super (OrderStatusForm,self ).__init__(*args,**kwargs)
        user=get_current_user()
        self.fields['sales_manager'].queryset = Sales_Manager.objects.filter(user=user)
    class Meta: 
        model = Order_Status
        exclude = ('user',)

class EmailForm(forms.Form): 
    description = forms.CharField(widget = forms.Textarea) 
    
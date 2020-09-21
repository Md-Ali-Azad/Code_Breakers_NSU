from django.urls import path,include
from django.contrib.auth import views as auth_views

from .views import *

app_name = 'accounting'
urlpatterns = [
    path('create/',completted_order_create,name='create'),
    path('list/',show,name='list'),
    path('bill_create/',bill_create,name='billcreate'),
    path('bill_list/',show_billing_list,name='bill_list'),
    path('payment_create/',payment_create,name='paymentcreate'),
    path('payment_list/',payment_list,name='payment_list'),
    path('calculation/<int:id>/',calculated,name='calculation'),
] 

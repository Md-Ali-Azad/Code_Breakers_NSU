
# Create your views here.
from django.shortcuts import render
from .forms import *
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from .models import *
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from controller.models import Vendors
from django.db.models import Q 
from django.contrib import messages
from controller.decorator import Employeeonly, Owneronly, Vendoronly, Customeronly
from django.contrib.auth.decorators import login_required

@Employeeonly
@login_required(login_url="/")
def create_product(request):
    forms = ProductForm()
    if request.method == 'POST':
        forms = ProductForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'New Product is Added successfully')
            return redirect('controller:inventory:product-list')
    context = {
        'form': forms
    }
    return render(request, 'create_product.html', context)



@Employeeonly
@login_required(login_url="/")
def ProductListView(request):
    if request.method == 'GET':
        context={
            'product':Product.objects.all()
        }
        
    return render(request, 'product_list.html', context)




@Employeeonly
@login_required(login_url="/")
def create_order(request):
    forms = OrderForm()
    if request.method == 'POST':
        forms = OrderForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'New Order is Added successfully')
            return redirect('controller:inventory:order-list')
    context = {
        'form': forms
    }
    return render(request, 'create_order.html', context)



@Employeeonly
@login_required(login_url="/")
def OrderListView(request):
    if request.method == 'GET':
        context={
            'order':Order.objects.all()
        }
        
    return render(request, 'order_list.html', context)
    


@Employeeonly
@login_required(login_url="/")
def create_delivery(request):
    forms = DeliveryForm()
    if request.method == 'POST':
        forms = DeliveryForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'New Delivery is Added successfully')
            return redirect('controller:inventory:delivery-list')
    context = {
        'form': forms
    }
    return render(request, 'create_delivery.html', context)



@Employeeonly
@login_required(login_url="/")
def DeliveryListView(request):
    if request.method == 'GET':
        context={
            'delivery':Delivery.objects.all()
        }
        
    return render(request, 'delivery_list.html', context)
    
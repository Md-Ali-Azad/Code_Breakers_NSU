
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
from django.shortcuts import Http404, get_object_or_404


@Vendoronly
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

@Vendoronly
@login_required(login_url="/")
def ProductListView(request):
    if request.method == 'GET':
        context={
            'product':Product.objects.filter(user=request.user)
        }
        
    return render(request, 'product_list.html', context)


@Vendoronly
@login_required(login_url="/")
def DeleteProduct(request, id):
    dlist = Product.objects.get(id=id)
    messages.warning(request, 'Product is deleted successfully')
    dlist.delete()  
    return redirect("controller:inventory:product-list")

@Vendoronly
@login_required(login_url="/")
def EditProduct(request, id):
    post = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'product is updated successfully')
        return redirect('controller:inventory:product-list')
    context={'form':form,'p_ac':'active'}
    return render(request,"inventory/editproduct.html", context)







@Vendoronly
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


@Vendoronly
@login_required(login_url="/")
def OrderListView(request):
    if request.method == 'GET':
        context={
            'order':Order.objects.filter(user=request.user)
        }
        
    return render(request, 'order_list.html', context)

@Vendoronly
@login_required(login_url="/")
def DeleteOrder(request, id):
    dlist = Order.objects.get(id=id)
    messages.warning(request, 'Order is deleted successfully')
    dlist.delete()  
    return redirect("controller:inventory:order-list")

@Vendoronly
@login_required(login_url="/")
def EditOrder(request, id):
    post = get_object_or_404(Order, id=id)
    form = OrderForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Order is updated successfully')
        return redirect('controller:inventory:order-list')
    context={'form':form}
    return render(request,"inventory/editorder.html", context)








@Vendoronly
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

@Vendoronly
@login_required(login_url="/")
def DeliveryListView(request):
    if request.method == 'GET':
        context={
            'delivery':Delivery.objects.filter(user=request.user)
        }
        
    return render(request, 'delivery_list.html', context)

@Vendoronly
@login_required(login_url="/")
def DeleteDelivery(request, id):
    dlist = Delivery.objects.get(id=id)
    messages.warning(request, 'Delivery is deleted successfully')
    dlist.delete()  
    return redirect("controller:inventory:delivery-list")

@Vendoronly
@login_required(login_url="/")
def EditDelivery(request, id):
    post = get_object_or_404(Delivery, id=id)
    form = DeliveryForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Delivery is updated successfully')
        return redirect('controller:inventory:delivery-list')
    context={'form':form}
    return render(request,"inventory/editdelivery.html", context)

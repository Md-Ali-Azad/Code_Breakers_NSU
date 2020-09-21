from django.shortcuts import render
from django.shortcuts import render,redirect
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from .models import *
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from .forms import ProductForm
from controller.models import Customer
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="/")
def show(request):  
    product_p = Product_Price.objects.all() 
    return render(request,"show_products_price.html",{'product_p':product_p})

@login_required(login_url="/")
def productandprice(request):  
    if request.method == "POST":  
        form = ProductForm(request.POST)  
        if form.is_valid():    
            form.save()  
            return redirect('controller:pos:productpricelist')  
        else:
            return render(request,'create_product_price.html',{'form':form}) 
    else:  
        form = ProductForm()  
    return render(request,'create_product_price.html',{'form':form})

@login_required(login_url="/")
def update(request, id):
    product_p = Product_Price.objects.get(id=id)  
    form = ProductForm(instance = product_p) 
    if request.method == "POST":
        form = ProductForm(request.POST, instance = product_p)   
        if form.is_valid():  
            form.save()  
            return HttpResponseRedirect(reverse('controller:pos:productpricelist'))   
    return render(request,'create_product_price.html',{'form':form})  

@login_required(login_url="/")
def delete(request, id):  
    product_p = Product_Price.objects.get(id=id)
    if product_p:  
        product_p.delete()  
    return HttpResponseRedirect(reverse('controller:pos:productpricelist'))

@login_required(login_url="/")
def seller_show(request):
    product_p = Product_Price.objects.all() 
    return render(request,"show_products_price.html",{'product_p':product_p,'seller':'seller'}) 

@login_required(login_url="/")
def order(request,id):
    product = Product_Price.objects.get(id=id)
    return render(request,'invoice.html',{'product':product})

@login_required(login_url="/")
def order_accepted(request,id):
    if hasattr(request.user, 'customer'):
        customer =  request.user.customer
        product = Product_Price.objects.get(id=id)
        context = {
            'before_purchasing_bkash_balance' : customer.bkash_balance,
            'after_purchasing_balance' : customer.bkash_balance-product.Product_price
        }
        return render(request,'orderensuring.html',context)
    return HttpResponse('you should register as custormer')

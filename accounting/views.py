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
from .forms import complete_order_form,bill_form,payment_form
from django.contrib.auth.decorators import login_required
from controller.decorator import Employeeonly, Owneronly


@login_required(login_url="/")
def show(request):  
    complete_order = Completed_Order.objects.all() 
    return render(request,"complete_order_productlist.html",{'complete_order': complete_order})

@login_required(login_url="/")
def completted_order_create(request):  
    if request.method == "POST":  
        form = complete_order_form(request.POST)  
        if form.is_valid():    
            form.save()  
            return redirect('controller:accounting:list')  
        else:
            return render(request,'completted_order_create.html',{'form':form}) 
    else:  
        form = complete_order_form()  
    return render(request,'completted_order_create.html',{'form':form})

@login_required(login_url="/")
def show_billing_list(request):  
    bill = Bill.objects.all() 
    return render(request,"bill_list.html",{'bill': bill})


@login_required(login_url="/")
def bill_create(request):  
    if request.method == "POST":  
        form = bill_form(request.POST)  
        if form.is_valid():    
            form.save()  
            return redirect('controller:accounting:bill_list')  
        else:
            return render(request,'bill_create.html',{'form':form}) 
    else:  
        form = bill_form()  
    return render(request,'bill_create.html',{'form':form})


@login_required(login_url="/")
def payment_list(request):  
    payment = Payment.objects.all() 
    return render(request,"payment_list.html",{'payment': payment})


@login_required(login_url="/")
def payment_create(request):  
    if request.method == "POST":  
        form = payment_form(request.POST)  
        if form.is_valid():    
            form.save()  
            return redirect('controller:accounting:payment_list')  
        else:
            return render(request,'payment_create.html',{'form':form}) 
    else:  
        form = payment_form()  
    return render(request,'payment_create.html',{'form':form})


@login_required(login_url="/")
def calculated(request,id):
    complete_order =Completed_Order.objects.filter(year=id)
    order_total = 0
    for i in complete_order:
        order_total = order_total+i.income

    bill = Bill.objects.filter(year=id)
    bill_total = 0
    for i in bill:
        bill_total = bill_total+i.cost

    payment = Payment.objects.filter(year=id)
    payment_total = 0
    for i in payment:
        payment_total = payment_total+i.cost

    profit = order_total-(bill_total+payment_total)
    context = {
        'year':id,
        'completted_order_income': order_total,
        'payment_cost':payment_total,
        'bill_cost':bill_total,
        'profit':profit,
    }
    return render(request,'calculation.html',context)

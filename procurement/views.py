from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from .models import *
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from .forms import OrderForm,OrderStatusForm,EmailForm
from controller.models import Vendors
from django.core.mail import send_mail

from django.db.models import Q 
from django.contrib import messages
from controller.decorator import Employeeonly, Owneronly, Vendoronly, Customeronly
from django.contrib.auth.decorators import login_required

@Employeeonly
@login_required(login_url="/")
def order_create(request): 
    if request.method == 'POST':
        o_form = OrderForm(request.POST,request.FILES)
        if o_form.is_valid():
            o_form.save()
            return HttpResponseRedirect(reverse('controller:procurement:orderlist'))
        else:
            return render(request, 'order_product.html', {'o_form':o_form})
    else:
        o_form = OrderForm()
    return render(request, 'order_product.html', {'o_form':o_form})


@Employeeonly
@login_required(login_url="/")
def order_list(request):
    if request.method == 'GET':
        context = {
            'Sales_Manager': Sales_Manager.objects.filter(deliverd=False)
        }
        return render(request, 'show_order.html',context)

@Employeeonly
@login_required(login_url="/")
def order_state(request): 
    if request.method == 'POST':
        o_form = OrderStatusForm(request.POST)
        if o_form.is_valid():
            o_form.save()
            return HttpResponseRedirect(reverse('controller:procurement:orderlist'))
        else:
            return render(request, 'order_status_form.html', {'o_form':o_form})
    else:
        o_form = OrderStatusForm()
    return render(request, 'order_status_form.html', {'o_form':o_form})

@Employeeonly
@login_required(login_url="/")
def order_status_list(request,id):
    if request.method == 'GET':
        if hasattr(Sales_Manager.objects.get(id=id), 'order_status'):
            context = {
                'Order_Status': Sales_Manager.objects.get(id=id).order_status
            }
            return render(request, 'order_status.html',context)
        else:
            return HttpResponse("it's order status dont created")

@Employeeonly
@login_required(login_url="/")
def order_status_list_all(request):
    q=Sales_Manager.objects.all()
    context = {
    'Order_Status': q
    }
    return render(request, 'order_status_show_all.html',context)

@Employeeonly
@login_required(login_url="/")
def Deliverd_Product(request,id):
    if request.method == 'GET':
        
        s = Sales_Manager.objects.get(id=id)
        s.deliverd = True
        s.save()
        context = {
            'Sales_Manager': Sales_Manager.objects.filter(deliverd = True)
        }
        return render(request, 'show_order.html',context)

@Employeeonly
@login_required(login_url="/")
def Order_vendor(request):
    if request.method == 'GET':
        q=User.objects.filter(groups__name='Vendor')
        context = {
            'vendors': q
        }
        #print(q.vprofile_Image)
    return render(request, 'vendors_list.html',context)

@Employeeonly
@login_required(login_url="/")
def Send_vendor(request):
    if request.method == 'GET':
        f = EmailForm()

    return render(request, 'send_vendor.html',{'form':f})


@Employeeonly
@login_required(login_url="/")
def Mail(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            send_mail(
            'Material Need',
            form.cleaned_data['description'],
            'ashik129603@gmail.com',
            ['ashik2015540@outlook.com'],
            fail_silently= False,
            )
        
            return HttpResponse('success')
        else:
            return HttpResponse('dont success')
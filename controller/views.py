from django.shortcuts import render,redirect
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from .models import *
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.shortcuts import Http404, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash 
from django.db.models import Q 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import *
from .forms import *


@login_required(login_url="/")
def home(request):
    context={
        'Hello':'hello'
    }
    return render(request,"home.html", context)


def success(request):
    return render(request, 'success.html')


def signup(request):
    if request.method == 'POST':
        u_form = SignUpForm(request.POST)
        p_form = CustomerForm(request.POST,request.FILES)  
        v_form = VendorsForm(request.POST,request.FILES)
        ce_form = CEForm(request.POST,request.FILES)
        if (u_form.is_valid() and p_form.is_valid()) or (u_form.is_valid() and v_form.is_valid()) or (u_form.is_valid() and ce_form.is_valid()):
            user = u_form.save()
            
            p_form = p_form.save(commit=False)
            p_form.user = user
            p_form.save()
            
            v_form = v_form.save(commit=False)
            v_form.user = user
            v_form.save()

            ce_form = v_form.save(commit=False)
            ce_form.user = user
            ce_form.save()

            messages.success(request, 'You have registered successfully. Please, wait for the confirmation mail')
            return redirect('/signup')
    else:
        u_form = SignUpForm(request.POST)
        p_form = CustomerForm(request.POST)
        v_form = VendorsForm(request.POST)
        ce_form = CEForm(request.POST)
    return render(request, 'signup.html', {'u_form': u_form, 'p_form': p_form, 'v_form':v_form, 'ce_form':ce_form})

def emp(request):  
    if request.method == "POST":  
        form = VendorsForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = VendorsForm()  
    return render(request,'index.html',{'form':form})  

def show(request):  
    vendors = Vendors.objects.all() 
    return render(request,"show_products.html",{'vendors':vendors})  

def edit(request, id):  
    vendor = Vendors.objects.get(id=id)  
    return render(request,'edit_product.html', {'vendor':vendor,'v_form':VendorsForm(instance=vendor)})  

def update(request, id):  
    vendor = Vendors.objects.get(id=id)  
    form = VendorsForm(request.POST, instance = vendor)  
    if form.is_valid():  
        form.save()  
        return HttpResponseRedirect(reverse('controller:show'))   
    return render(request, 'edit.html', {'vendor':vendor,'v_form':VendorsForm()})  

def delete(request, id):  
    vendor = Vendors.objects.get(id=id)
    if vendor:  
        vendor.delete()  
    return HttpResponseRedirect(reverse('controller:show'))  

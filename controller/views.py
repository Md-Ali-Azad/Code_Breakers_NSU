from django.shortcuts import render,redirect
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from .models import *
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm


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
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from controller.decorator import Owneronly, Vendoronly, Customeronly, Employeeonly




@login_required(login_url="/")
def news(request):
	if request.method == "POST":  
		form = NewsForm(request.POST)  
		if form.is_valid():  
			try:
				form.save()
				messages.success(request, 'New Post is Added successfully')
				return redirect('/news/news')
			except:
				pass
				
	else:
		form = NewsForm()
		
	nlist = News.objects.order_by('ncreated_at').filter(user=request.user).reverse()   
	paginator = Paginator(nlist, 3) 
	page = request.GET.get('page')
	nlist_show = paginator.get_page(page)
	args={'news': 'active','news1':'active' ,'form': form, 'nlist':nlist, 'nlist_show': nlist_show}
	return render(request, "news/news.html", args)

@login_required(login_url="/")
def allnews(request):
	nlist = News.objects.order_by('ncreated_at').reverse()   
	paginator = Paginator(nlist, 3) 
	page = request.GET.get('page')
	nlist_show = paginator.get_page(page)
	args={'news': 'active', 'news11':'active' , 'nlist':nlist, 'nlist_show': nlist_show}
	return render(request, "news/newsforall.html", args)

@login_required(login_url="/")
def ndelete(request, id):  
	nlist = News.objects.get(id=id)  
	nlist.delete()  
	messages.warning(request, 'Post is deleted successfully')
	return redirect("/news/news")

@login_required(login_url="/")
def nedit(request, id):  
	post = get_object_or_404(News, id=id)
	form = NewsForm(request.POST or None, request.FILES or None, instance=post)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, 'Post is updated successfully')
		return redirect('/news/news')
	return render(request, 'news/newsedit.html', {"form": form,'news': 'active'})

@login_required(login_url="/")
def newscomments(request, id):
	nlist = News.objects.get(id=id)
	return render(request,'news/newscomments.html', {'nlist':nlist, 'news': 'active'})









@login_required(login_url="/")
def home(request):
    context={
        'Hello':'hello',
        'ach':'active',
    }
    return render(request,"home.html", context)






############------Accounts------#############
@login_required(login_url="/")
def profile(request):
    return render(request, 'account/profile.html', {'pro':'active'})

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

            ce_form = ce_form.save(commit=False)
            ce_form.user = user
            ce_form.save()

            messages.success(request, 'You have registered successfully. Please, wait for the confirmation mail')
            return redirect('/signup')
    else:
        u_form = SignUpForm(request.POST)
        p_form = CustomerForm(request.POST)
        v_form = VendorsForm(request.POST)
        ce_form = CEForm(request.POST)
    return render(request, 'signup.html', {'u_form': u_form, 'p_form': p_form, 'v_form':v_form, 'ce_form':ce_form, 'ac':'active'})

@login_required(login_url="/")
def profileedit(request):  
    if request.user.groups.filter(name='Vendor').exists():
        u_form = UpdateForm(request.POST or None, request.FILES or None, instance=request.user)
        v_form = VendorsForm(request.POST or None, request.FILES or None, instance=request.user.vendors)
        if u_form.is_valid() and v_form.is_valid():
            user = u_form.save()
            v_form = v_form.save(commit=False)
            v_form.user = user
            v_form.save()
            messages.success(request, 'Profile is updated successfully')
            return redirect('/profile')
        context={'u_form': u_form, 'v_form':v_form, 'pe_ac':'active'}
        
    elif request.user.groups.filter(name='Customer').exists():
        u_form = UpdateForm(request.POST or None, request.FILES or None, instance=request.user)
        p_form = CustomerForm(request.POST or None, request.FILES or None, instance=request.user.customer)
        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save()
            p_form = p_form.save(commit=False)
            p_form.user = user
            p_form.save()
            messages.success(request, 'Profile is updated successfully')
            return redirect('/profile')
        context={'u_form': u_form, 'p_form': p_form,  'pe_ac':'active'}
        
    else:
        u_form = UpdateForm(request.POST or None, request.FILES or None, instance=request.user)
        ce_form = CEFormUpdate(request.POST or None, request.FILES or None, instance=request.user.company_employee)
        if u_form.is_valid() and ce_form.is_valid():
            user = u_form.save()
            ce_form = ce_form.save(commit=False)
            ce_form.user = user
            ce_form.save()
            messages.success(request, 'Profile is updated successfully')
            return redirect('/profile')
        context={'u_form': u_form, 'ce_form':ce_form, 'pe_ac':'active'}

    return render(request, 'account/reg_form_edit.html', context)

@login_required(login_url="/")
def change_password(request):
    if request.method=='POST':
        form = PasswordChangeForm(data=request.POST, user=request.user) #not instance

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password Changed Successfully')
            return redirect('/profile')
        else:
            messages.success(request, 'Please, Provide a valid password')
    else:
        form = PasswordChangeForm(user=request.user)
    context={'form':form, 'p_ac':'active'}
    return render(request, 'account/change_password.html', context)











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

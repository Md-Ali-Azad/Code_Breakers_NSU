from django.http import HttpRequest
from django.shortcuts import redirect



def Owneronly(view_func):
    def wrapper_function(request, *args, **kwargs):
        group=None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group=='Owner':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('/')
    return wrapper_function





def Vendoronly(view_func):
    def wrapper_function(request, *args, **kwargs):
        group=None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group=='Vendor':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('/')
    return wrapper_function



def Customeronly(view_func):
    def wrapper_function(request, *args, **kwargs):
        group=None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group=='Customer':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('/')
    return wrapper_function



def Employeeonly(view_func):
    def wrapper_function(request, *args, **kwargs):
        group=None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group=='Employee':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('/')
    return wrapper_function
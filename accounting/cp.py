from accounting.models import *
from django.shortcuts import render
from django.shortcuts import render,redirect

def yoverview(request):
    q=Completed_Order.objects.all()
    return({'q':q})
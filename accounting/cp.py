from accounting.models import *
from django.shortcuts import render
from django.shortcuts import render,redirect

def yoverview(request):
    q=Completed_Order.objects.values_list('year',flat=True).order_by('year').distinct()
    return({'q':q})
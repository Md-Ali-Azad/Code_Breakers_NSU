from django.db import models
from django.contrib.auth.models import User
from django_currentuser.db.models import CurrentUserField

# Create your models here.
class Completed_Order(models.Model):
    user = CurrentUserField()
    order_name = models.CharField(max_length=200, blank=True,null=True, verbose_name="Order Name or Code")
    income = models.DecimalField(max_digits=10, decimal_places=2,null= True,blank = True)
    year =  models.PositiveIntegerField(null= True,blank= True)
    Created_at = models.DateTimeField(auto_now_add=True, null=True)
    Updated_at= models.DateTimeField(auto_now=True)

class Bill(models.Model):
    user = CurrentUserField()
    bill_name = models.CharField(max_length=200, blank=True,null=True, verbose_name="Bill Name or Code")
    cost = models.DecimalField(max_digits=10, decimal_places=2,null= True,blank = True)
    year =  models.PositiveIntegerField(null= True,blank= True)
    Created_at = models.DateTimeField(auto_now_add=True, null=True)
    Updated_at= models.DateTimeField(auto_now=True)

class Payment(models.Model):
    user = CurrentUserField()
    payment_name = models.CharField(max_length=200, blank=True,null=True, verbose_name="Payment Name or Code")
    cost = models.DecimalField(max_digits=10, decimal_places=2,null= True,blank = True)
    year =  models.PositiveIntegerField(null= True,blank= True)
    Created_at = models.DateTimeField(auto_now_add=True, null=True)
    Updated_at= models.DateTimeField(auto_now=True)
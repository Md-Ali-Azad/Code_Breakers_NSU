from django.db import models
from django.contrib.auth.models import User
from django_currentuser.db.models import CurrentUserField

class Product_Price(models.Model):
    Product_Name = models.CharField(max_length=200, blank=True,null=True)
    Product_price = models.DecimalField(max_digits=6, decimal_places=2,null=True,blank=True)
    




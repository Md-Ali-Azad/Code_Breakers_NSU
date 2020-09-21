from django.db import models
from django.contrib.auth.models import User
from django_currentuser.db.models import CurrentUserField

class Product_Price(models.Model):
    user=CurrentUserField()
    Product_Name = models.CharField(max_length=200, blank=True,null=True)
    Product_price = models.DecimalField(max_digits=6, decimal_places=2,null=True,blank=True)
    

class VendorsCustomer(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    user = CurrentUserField()
    institution_name = models.CharField(max_length=200, blank=True, verbose_name="Instituion Name")
    institution_id = models.CharField(max_length=200, blank=True, verbose_name="Instituion ID")
    address=models.CharField(max_length=500,verbose_name="Address", blank=True)
    contact = models.CharField(verbose_name="Contact",max_length=20, blank=True, default='N/A')
    profile_Image = models.ImageField(verbose_name="Profile Image",upload_to = 'Vendor_Customer_Profile_Pic/', default = 'https://icon-library.net/images/young-person-icon/young-person-icon-7.jpg', blank=True)
    gender =  models.CharField(verbose_name="Gender",max_length=2, choices=GENDER_CHOICES, blank=False, default='M')
    Created_at = models.DateTimeField(auto_now_add=True)
    Updated_at= models.DateTimeField(auto_now=True)


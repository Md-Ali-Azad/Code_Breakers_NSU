from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django_currentuser.db.models import CurrentUserField


class Raw_Materials(models.Model):
    rm=models.CharField(verbose_name="Raw Materials", max_length=100)
    created_at= models.DateTimeField(auto_now_add=True)

class Designation(models.Model):
    designaiton=models.CharField(max_length=150)
    created_at= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.designaiton


class News(models.Model):
    user = CurrentUserField() 
    ntitle=models.CharField(max_length=500, default='NSU Garment System', verbose_name="News Title")
    ndetails = RichTextUploadingField(verbose_name="News Details")
    ncreated_at= models.DateTimeField(auto_now_add=True)
    nupdated_at=models.DateTimeField(auto_now=True)
    class Meta:  
        db_table = "news"  
    def __str__(self):
        return self.ndetails


class Customer(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    institution_name = models.CharField(max_length=200, blank=True, verbose_name="Instituion Name")
    institution_id = models.CharField(max_length=200, blank=True, verbose_name="Instituion ID")
    caddress=models.CharField(max_length=500,verbose_name="Address", blank=True)
    ccontact = models.CharField(verbose_name="Contact",max_length=20, blank=True, default='N/A')
    cprofile_Image = models.ImageField(verbose_name="Profile Image",upload_to = 'Customer_Profile_Pic/', default = 'https://icon-library.net/images/young-person-icon/young-person-icon-7.jpg', blank=True)
    cgender =  models.CharField(verbose_name="Gender",max_length=2, choices=GENDER_CHOICES, blank=False, default='M')
    cemail_confirmed = models.BooleanField(verbose_name="Email Confirmation",default=False)
    Updated_at= models.DateTimeField(auto_now=True)

class Vendors(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200, blank=True, verbose_name="Company Name")
    company_id = models.CharField(max_length=200, blank=True, verbose_name="Company ID")
    vaddress=models.CharField(max_length=500,verbose_name="Address", blank=True)
    vcontact = models.CharField(verbose_name="Contact",max_length=20, blank=True, default='N/A')
    vprofile_Image = models.ImageField(verbose_name="Profile Image",upload_to = 'Vendor_Profile_Pic/', default = 'https://icon-library.net/images/young-person-icon/young-person-icon-7.jpg', blank=True)
    vgender =  models.CharField(verbose_name="Gender",max_length=2, choices=GENDER_CHOICES, blank=False, default='M')
    vemail_confirmed = models.BooleanField(verbose_name="Email Confirmation",default=False)
    Updated_at= models.DateTimeField(auto_now=True)



class Company_Employee(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    card_No= models.CharField(max_length=200, blank=True, verbose_name="Card No.")
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE,blank=True)
    eaddress=models.CharField( max_length=500,verbose_name="Address", blank=True)
    econtact = models.CharField(verbose_name="Contact",max_length=20, blank=True, default='N/A')
    eprofile_Image = models.ImageField(verbose_name="Profile Image",upload_to = 'Employee_Profile_Pic/', default = 'https://icon-library.net/images/young-person-icon/young-person-icon-7.jpg', blank=True)
    egender =  models.CharField(verbose_name="Gender",max_length=2, choices=GENDER_CHOICES, blank=False, default='M')
    eemail_confirmed = models.BooleanField(verbose_name="Email Confirmation",default=False)
    Updated_at= models.DateTimeField(auto_now=True)
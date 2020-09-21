from django.db import models

# Create your models here.
from django.db import models
from django_currentuser.db.models import CurrentUserField
# Create your models here.
class Sales_Manager(models.Model):
    user = CurrentUserField() 
    order_code = models.CharField(max_length=11, blank=True, null=True)
    product_name = models.CharField(max_length=11, blank=True, null=True)
    product_quantity = models.PositiveIntegerField(blank=True, null=True)
    product_picture = models.ImageField(upload_to='image/')
    product_colour = models.CharField(max_length=11, blank=True, null=True)
    description = models.TextField()
    deliverd  = models.BooleanField(default=False,blank=True, null=True)
    def __str__(self):
        return self.order_code

class Order_Status(models.Model):
    STATUS_CHOICES = (
        ('D', 'Done'),
        ('P', 'Pending'),

    )
    user = CurrentUserField() 
    sales_manager = models.OneToOneField(Sales_Manager, on_delete=models.CASCADE,blank=True, null=True, verbose_name="Order Code")
    order_recived =  models.CharField(max_length=2, choices=STATUS_CHOICES, blank=False, default='D', verbose_name="Order Received")
    raw_materials_collection = models.CharField(max_length=2, choices=STATUS_CHOICES, blank=False, default='D')
    production_stage1 = models.CharField(max_length=2, choices=STATUS_CHOICES, blank=False, default='D')
    production_stage2 = models.CharField(max_length=2, choices=STATUS_CHOICES, blank=False, default='D')
    packing = models.CharField(max_length=2, choices=STATUS_CHOICES, blank=False, default='D')
    shipping = models.CharField(max_length=2, choices=STATUS_CHOICES, blank=False, default='D')
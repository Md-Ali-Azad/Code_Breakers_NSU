from django.db import models

# Create your models here.
from django.db import models
from django_currentuser.db.models import CurrentUserField
# Create your models here.
class Product(models.Model):
    user = CurrentUserField() 
    name = models.CharField(max_length=120, unique=True)
    quantity = models.PositiveIntegerField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICE = (
        ('p', 'Pending'),
        ('c', 'Complete'),
    )
    user = CurrentUserField() 
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    design = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    buyer = models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE,default='p')
    created_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.product.name


class Delivery(models.Model):
    user = CurrentUserField() 
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    courier_name = models.CharField(max_length=120)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.courier_name
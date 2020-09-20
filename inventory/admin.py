from django.contrib import admin
from inventory.models import *
# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Delivery)
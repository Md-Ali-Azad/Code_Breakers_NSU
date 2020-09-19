from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from controller.models import *



class CProfileInline(admin.StackedInline):
    model = Customer
    can_delete = False

class VProfileInline(admin.StackedInline):
    model = Vendors
    can_delete = False

class EProfileInline(admin.StackedInline):
    model = Company_Employee
    can_delete = False

class UserAdmin(UserAdmin):
    inlines = (CProfileInline, VProfileInline, EProfileInline)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active')

admin.site.unregister(User)  
admin.site.register(User, UserAdmin) 
admin.site.register(Designation)
admin.site.register(Raw_Materials)


admin.site.register(Vendors)
admin.site.register(Customer)
admin.site.register(Company_Employee)
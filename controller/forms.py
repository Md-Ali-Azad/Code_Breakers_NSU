from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Please, give a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [ 'institution_name','institution_id','caddress','ccontact','cprofile_Image','cgender']

class VendorsForm(forms.ModelForm):
    class Meta:
        model = Vendors
        fields = [ 'company_name','company_id','vaddress','vcontact','vprofile_Image','vgender']

class CEForm(forms.ModelForm):
    class Meta:
        model = Company_Employee
        fields = [ 'card_No','designation','eaddress','econtact','eprofile_Image','egender']

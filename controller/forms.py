from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class NewsForm(forms.ModelForm):
    #ntitle = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':' News Title'}),required=True,max_length=500)
    #ndetails= forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:  
        model = News  
        fields = ('ntitle', 'ndetails')



class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Please, give a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class UpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', )


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [ 'institution_name','institution_id','caddress','ccontact','cprofile_Image','cgender']

class VendorsForm(forms.ModelForm):
    class Meta:
        model = Vendors
        fields = [ 'company_name','company_id','vaddress','vcontact','vprofile_Image','vgender']

class CEForm(forms.ModelForm):
    designation = forms.ModelChoiceField(queryset=Designation.objects, empty_label=None)
    class Meta:
        model = Company_Employee
        fields = [ 'card_No','designation','eaddress','econtact','eprofile_Image','egender']



class CEFormUpdate(forms.ModelForm):
    class Meta:
        model = Company_Employee
        fields = [ 'card_No','eaddress','econtact','eprofile_Image','egender']



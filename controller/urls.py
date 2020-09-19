from django.urls import path,include
from django.contrib.auth import views as auth_views

from .views import *

app_name = 'controller'
urlpatterns = [
    path('home/',home,name='home'),
    path('', auth_views.LoginView.as_view(redirect_authenticated_user=True,template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page= 'controller:login'), name='logout'),
    path('signup/',signup, name='signup'),
    path('success/', success, name='success'),
    path('show/',show,name='show'),
    path('edit/<int:id>',edit,name='edit'),
    path('update/<int:id>',update,name='update'),
    path('delete/<int:id>',delete,name='delete'),
] 

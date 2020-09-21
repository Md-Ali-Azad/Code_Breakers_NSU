from django.urls import path,include
from django.contrib.auth import views as auth_views

from .views import *

app_name = 'controller'
urlpatterns = [
    path('home/',home,name='home'),
    path('', auth_views.LoginView.as_view(redirect_authenticated_user=True,template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page= 'controller:login'), name='logout'),
    path('signup/',signup, name='signup'),
    path('profile/', profile, name='profile'),
    path('change_password/', change_password, name="change_password"),
    path('profileedit/', profileedit, name="profileedit"),

    ########------News Section-----########
    path('news/news/', news, name="news"),
    path('news/newsall/', allnews, name="allnews"),
    path('news/nedit/<int:id>/', nedit, name="nedit"),
    path('news/ndelete/<int:id>/', ndelete, name="ndelete"), 
    path('news/newscomments/<int:id>/', newscomments, name="newscomments"),



    ##########-----App Connection------#########
    path('procurement/',include('procurement.urls',namespace="procurement")),
    path('inventory/',include('inventory.urls',namespace="inventory")),
    path('pos/',include('pos.urls',namespace="pos")),
    path('accounting/',include('accounting.urls',namespace="accounting")),

    path('show/',show,name='show'),
    path('edit/<int:id>',edit,name='edit'),
    path('update/<int:id>',update,name='update'),
    path('delete/<int:id>',delete,name='delete'),
] 

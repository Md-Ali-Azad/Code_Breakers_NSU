from django.urls import path,include
from .views import *

app_name = 'procurement'
urlpatterns = [
    path('order_create/',order_create,name='ordercreate'),
    path('order_list/',order_list,name='orderlist'),
    path('order_status/',order_state,name='orderstatus'),
    path('order_status_list/<int:id>',order_status_list,name='orderstatuslist'),
    path('order_status_list_all/',order_status_list_all,name='orderstatuslistall'),
    path('deliver/<int:id>',Deliverd_Product,name='deliver'),
    path('order_vendor/',Order_vendor,name='ordervendor'),
    path('mail/',Mail,name='mail'),
    path('send_vendor/',Send_vendor,name='sendvendor')
] 
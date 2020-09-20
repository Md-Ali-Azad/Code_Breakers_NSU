from django.urls import path
from .views import *
app_name = 'inventory'
urlpatterns = [
    
    path('create-product/', create_product, name='create-product'),
    path('create-order/', create_order, name='create-order'),
    path('create-delivery/', create_delivery, name='create-delivery'),
    path('product-list/', ProductListView, name='product-list'),
    path('order-list/', OrderListView, name='order-list'),
    path('delivery-list/', DeliveryListView, name='delivery-list'),
]
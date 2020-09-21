from django.urls import path

from .views import *

app_name = 'pos'
urlpatterns = [
    path('add_product_price/',productandprice,name='addproductprice'),
    path('product_price_list/',show,name='productpricelist'),
    path('update/<int:id>',update,name='update'),
    path('delete/<int:id>',delete,name='delete'),
    path('seller_show/',seller_show,name='sellershow'),
    path('order/<int:id>',order,name='order'),
    path('order_accepted/<int:id>',order_accepted,name='orderaccepted')
] 
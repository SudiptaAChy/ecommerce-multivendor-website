from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyOrder, name='my_order'),
    path('list', views.OrderList, name='order_list'),
    path('info/<int:id>', views.OrderDetails, name='order_list'),
    path('myorder', views.SellerOrder, name='seller_order'),
]

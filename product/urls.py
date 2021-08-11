from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name='index'),
    path('details/<str:slug>', views.DetailPage, name='details'),
    path('addproduct', views.AddProduct, name='add_product'),
    path('allproducts', views.AllProducts, name='all_product'),
    path('discountproducts', views.DiscountProducts, name='discount_product'),
    path('topsell', views.BestSellingProducts, name='top_selling_product'),
    path('catagoryproducts/<str:cname>', views.CatagoryProducts, name='catagory_product'),
    path('search', views.SearchProducts, name='search_product'),
    path('cart/<str:pk>', views.AddCart, name='add_cart'),
    path('delete/<str:pk>', views.DeleteProduct, name='delete_product'),
    path('update/<str:pk>', views.UpdateProduct, name='update_product'),
    path('mycart/<int:id>', views.MyCart, name='my_cart'),
    path('mycart/remove/<int:id>', views.RemoveProd, name='remove_product'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('login', views.LoginUser, name='login'),
    path('logout/', views.LogoutUser, name='logout'),
    path('create/', views.CreateUser, name='create'),
    path('dashboard/', views.DashBoard, name='dashboard'),
    path('myproducts/', views.DashBoard, name='dashboard'),
]

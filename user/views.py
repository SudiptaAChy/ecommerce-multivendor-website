from django.contrib.auth.backends import UserModel
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import UserInfo
from product.models import Product

def LoginUser(request) :
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None :
            login(request, user)
            return redirect('/')
        else :
            messages.error(request, 'Invalid login!')
    return render(request, 'index.html')

def LogoutUser(request) :
    if request.method == 'GET' :
        logout(request)
        messages.success(request, 'Logout successfully!')
        return redirect('/')
    
def CreateUser(request) :
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']
        fname = request.POST['fname']
        lname = request.POST['lname']
        phone = request.POST['phone']
        type = request.POST.get('type1')
        if User.objects.filter(username=username).exists() :
            messages.error(request, 'This email already exists, try another!')
            return redirect('/user/create/')
        else :
            user = User.objects.create_user(username=username, password=password)
            user.save()
            userInfo = UserInfo(user=user, fname=fname, lname=lname, phone=phone, type=type)
            userInfo.save()
            return redirect('/')
    return render(request, 'signup.html')

def DashBoard(request) :
    if request.method == 'GET' :
        all_products = Product.objects.filter(user = request.user).all()
        context = {
            'all_products' : all_products,
        }
        return render(request, 'myproducts.html', context)
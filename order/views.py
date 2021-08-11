from product.models import Cart, Product
from django.shortcuts import redirect, render
from .models import OrderInfo

def MyOrder(requst) :
    if requst.method == 'POST' :
        user = requst.user
        products = Cart.objects.filter(buyer=requst.user).all()
        name = requst.POST['name']
        phone = requst.POST['phone']
        email = requst.POST['email']
        address = requst.POST['address']
        for pd in products :
            prod = OrderInfo(user=user, product=pd.product, quantity=pd.quantity, price=pd.price, name=name, phone=phone, email=email, address=address)
            prod.save()
        Cart.objects.filter(buyer=requst.user).delete()
        return redirect('/order/list')

def OrderList(request) :
    products = OrderInfo.objects.filter(user=request.user).all()
    context = {
        'all_products' : products,
    }
    return render(request, 'my_order.html', context)

def OrderDetails(request, id) :
    product = OrderInfo.objects.get(id=id)
    context = {
        'product' : product,
    }
    return render(request,'order_info.html', context)

def SellerOrder(request) :
    orders = OrderInfo.objects.filter(product__user=request.user)
    context = {
        'orders' : orders,
    }
    return render(request, 'seller_order.html', context)
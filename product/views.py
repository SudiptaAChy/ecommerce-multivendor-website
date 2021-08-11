from review.models import Review
from product.models import Banner, Cart, Product, Catagory, ProductImages
from django.shortcuts import get_object_or_404, redirect, render
from user.models import UserInfo
from .forms import AddProductFullForm
from django.contrib import messages
from django.views.generic.edit import UpdateView
from order.models import OrderInfo
from django.db.models import Count

def HomePage(request) :
    if request.method == 'GET' :
        banners = Banner.objects.all()
        catagories = Catagory.objects.all()
        all_products = Product.objects.all()[0:6]
        discount_products = Product.objects.exclude(discount=0.00).order_by('-discount')[:6]
        best_selling = OrderInfo.objects.annotate(consumption_times=Count('product')).order_by('consumption_times')[0:6]
        if request.user.is_authenticated:
            userinfo = UserInfo.objects.get(user=request.user)
        else :
            userinfo = None
        context = {
            'banners' : banners,
            'catagories' : catagories,
            'all_products' : all_products,
            'userinfo' : userinfo,
            'discount_products' : discount_products,
            'best_selling' : best_selling,
        }
        return render(request, 'index.html', context)
    
def DetailPage(request, slug) :
    if request.method == 'GET' :
        product = Product.objects.get(slug = slug)
        all_reviews = Review.objects.filter(product=product)
        context = {
            'product' : product,
            'all_reviews' : all_reviews,
        }
        return render(request, 'details.html', context)
    elif request.method == 'POST' :
        return redirect(request, '/')
    
def AddProduct(request) :
    if request.method == 'POST' :
        form = AddProductFullForm(request.POST or None, request.FILES or None)
        files = request.FILES.getlist('images')
        if form.is_valid() :
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            for f in files :
                ProductImages.objects.create(product=product, images=f)
            return redirect('/addproduct')
        else :
            messages.error(request, 'Form invalid!')
            return redirect('/addproduct')
    else :
        form = AddProductFullForm()
    context = {
        'form' : form,
    }
    return render(request, 'addproduct.html', context)

def AllProducts(request) :
    if request.method == 'GET' :
        all_products = Product.objects.all()
        context = {
            'all_products' : all_products,
        }
    return render(request, 'allproducts.html', context)

def DiscountProducts(request) :
    if request.method == 'GET' :
        all_products = Product.objects.exclude(discount=0.00).order_by('-discount')
        context = {
            'all_products' : all_products,
        }
    return render(request, 'discountproducts.html', context)

def BestSellingProducts(request) :
    best_selling = OrderInfo.objects.annotate(consumption_times=Count('product')).order_by('consumption_times')
    context = {
        'all_products' : best_selling,
    }
    return render(request, 'top_selling.html', context)

def CatagoryProducts(request, cname) :
    if request.method == 'GET' :
        all_products = Product.objects.filter(catagory__name=cname)
        context = {
            'catagory' : cname,
            'all_products' : all_products,
        }
    return render(request, 'catagoryproducts.html', context)

def SearchProducts(request) :
    if request.method == 'POST' :
        data = request.POST["searchText"]
        all_products = Product.objects.filter(name__contains=data) | Product.objects.filter(details__contains=data)
        context = {
            'search' : data,
            'all_products' : all_products,
        }
    return render(request, 'search.html', context)

def AddCart(request, pk) :
    if request.method == 'POST' :
        product = Product.objects.get(id=pk)
        user = request.user
        quantity = request.POST['quantity']
        price = int(quantity) * float(product.price)
        cart = Cart(product=product, buyer=user, quantity=quantity, price=price)
        cart.save()
    return redirect('/')

def DeleteProduct(request, pk) :
    if request.method == 'GET' :
        product = Product.objects.get(id=pk)
        product.delete()
        messages.success(request, 'Product deleted successfully!')
        return redirect('/')

def UpdateProduct(request, pk) :
    obj = get_object_or_404(Product, id=pk)
    form = AddProductFullForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid() :
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return redirect('/addproduct')
    context = {
        'form' : form,
    }
    return render(request, "addproduct.html", context)

# class UpdateProduct(UpdateView) :
#     model = Product
#     fields = ['catagory', 'name', 'details', 'price', 'discount', 'image',]
#     success_url = "/"
#     # template name = product/product_form.html

def MyCart(request, id) :
    products = Cart.objects.filter(buyer=id)
    totalTk = 0.0
    for p in products :
        totalTk = totalTk + float(p.price)
    totalOrder = len(products)
    context = {
        'total_order' : totalOrder,
        'total_tk' : totalTk,
        'all_products' : products,
    }
    return render(request, 'my_cart.html', context)

def RemoveProd(request, id) :
    cart = Cart.objects.get(id=id)
    cart.delete()
    messages.success(request, 'My cart product deleted successfully!')
    return redirect('/mycart/' + str(request.user.id))
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Review
from product.models import Product

def WriteReview(request, slug) :
    if request.method == 'POST' :
        comment = request.POST['cmnt']
        product = Product.objects.get(slug=slug)
        rev = Review(user=request.user, product=product, comment=comment)
        rev.save()
        return redirect('/details/' + str(slug))
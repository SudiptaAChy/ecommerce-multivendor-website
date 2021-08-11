from django.contrib import admin
from .models import Catagory, Banner, Product, ProductImages, Cart

admin.site.register(Catagory)
admin.site.register(Banner)
admin.site.register(Cart)

class ProductImagesAdmin(admin.StackedInline) :
    model = ProductImages
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin) :
    inlines = [ProductImagesAdmin] 
    class Meta:
       model = Product
       
@admin.register(ProductImages)
class ProductImagesAdmin(admin.ModelAdmin):
    pass
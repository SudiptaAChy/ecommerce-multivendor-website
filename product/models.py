from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Catagory(models.Model) :
    name = models.CharField(max_length=255)
    class Meta :
        ordering = ('name',)
    def __str__(self):
        return self.name
    
class Product(models.Model) :
    user = models.ForeignKey(User, related_name='user_name', on_delete=models.CASCADE)
    catagory = models.ForeignKey(Catagory, related_name='catagory_name', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=400, unique=True, blank=True, null=True, default="")
    details = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True, help_text='in %')
    image = models.ImageField(upload_to = 'uploads/', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    class Meta :
        ordering = ('-date_created',)
        
    def __str__(self) :
        return self.name
    
    def get_image(self) :
        if self.image :
            return 'http://127.0.0.1:8000' + self.image.url
        else :
            return ''
        
    def save(self, *args, **kwargs) :
        super(Product, self).save(*args, **kwargs)
        if not self.slug :
            self.slug = slugify(self.name) + '-' + str(self.id)
            if not self.discount :
                self.discount = 0.00
            self.save()
        # if not self.discount :
        #     self.discount = 0.0
        #     self.save()

class ProductImages(models.Model) :
    product = models.ForeignKey(Product, related_name='product_images', on_delete=models.CASCADE)
    images = models.ImageField(upload_to = 'uploads/', blank=True, null=True)
    
    def __str__(self) :
        return self.product.name


class Banner(models.Model) :
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to = 'uploads/', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    class Meta :
        ordering = ('-date_created',)
    
    def __str__(self) :
        return self.name
    
    def get_image(self) :
        if self.image :
            return 'http://127.0.0.1:8000' + self.image.url
        else :
            return ''


class Cart(models.Model) :
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True,)
    price = models.DecimalField(max_digits=40, decimal_places=2, null=True,)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    class Meta :
        ordering = ('-created_at',)
        
    def __str__(self):
        return str(self.product) + str(self.buyer)
    
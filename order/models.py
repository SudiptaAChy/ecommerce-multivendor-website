from product.models import Product
from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

class OrderInfo(models.Model) :
    STATUS = (
        ('Pending', 'Pending'),
        ('Order Received', 'Order Received'),
        ('Preparing', 'Preparing'),
        ('Onshiping', 'Onshiping'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True,)
    price = models.DecimalField(max_digits=40, decimal_places=2, null=True,)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.TextField()
    status = MultiSelectField(choices=STATUS, max_length=255, default='Pending', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    class Meta :
        ordering = ('-date_created',)
    def __str__(self):
        return str(self.user) + ' , ' + str(self.product)

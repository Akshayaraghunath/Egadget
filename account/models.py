from django.db import models
from django.contrib.auth.models import User

class Products(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    image=models.ImageField(upload_to='product_images')
    description=models.CharField(max_length=500)
    options=(
        ('Mobile Phone','Mobile Phone'),
        ('Earphone','Earphone'),
        ('Laptop','Laptop'),
        ('Tablet','tablet'),
        ('Smart Watch','smart Watch'),
        ('BT speaker','BT speaker')
    )
    category=models.CharField(max_length=200,choices=options,default='Mobile Phone')

class Cart(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    date=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=100,default='cart')
    @property
    def totalamnt(self):
        return self.product.price*self.quantity

class Order(models.Model):
    cart=models.OneToOneField(Cart,on_delete=models.CASCADE,related_name='cartorder')
    date=models.DateField(auto_now_add=True)
    address=models.CharField(max_length=500,null=True)
    phone=models.IntegerField(null=True)
    options=(
        ('Order Placed','Order Placed'),
        ('Shipped','Shipped'),
        ('Out For Deliver','Out For Deliver'),
        ('Delivered','Delivered'),
        ('Cancelled','Cancelled')
    )
    status=models.CharField(max_length=100,choices=options,default="order placed")


# Create your models here.

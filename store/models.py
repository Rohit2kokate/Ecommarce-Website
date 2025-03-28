from django.db import models
import datetime
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "category"
    

class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    phone_number=models.CharField(max_length=20)
    password=models.CharField(max_length=8)

    def __str__(self):
        return self.first_name +" "+self.last_name
    
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_price=models.DecimalField(max_digits=10,decimal_places=2)
    product_description=models.TextField()
    product_image=models.ImageField(upload_to='images/')
    product_category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    #Sale
    is_sale=models.BooleanField(default=False)
    sale_price=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.product_name

class Order(models.Model):
    choice=[
        ('pending','pending'),
        ('shipped','shipped'),
        ('delivered','delivered'),
        ('cancelled','cancelled'),
    ]
    product_name=models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    addres=models.CharField(max_length=50)
    phone_no=models.IntegerField()
    order_date = models.DateTimeField(default=datetime.datetime.now)
    order_status = models.CharField(max_length=100, default='pending',choices=choice)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f" {self.product_name} - Total: ${self.total_cost}"


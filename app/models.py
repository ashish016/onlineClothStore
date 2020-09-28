from django.db import models

# Create your models here.
class Customer(models.Model):
        customer_Id=models.CharField(max_length=10, primary_key="True")
        first_Name = models.CharField(max_length=10)
        last_Name = models.CharField(max_length=10)
        email = models.TextField(unique="true")
        password = models.TextField()
        type=models.CharField(max_length=10)
        def getPrimaryKey(self):
                return self.customer_Id
        def hello(self):
                return "Hello"


class Product(models.Model):
        product_Id=models.CharField(max_length=10, primary_key="True")
        product_Name= models.CharField(max_length=20)
        product_Price=models.FloatField()
        product_Quantity=models.IntegerField()
        upload_Id = models.CharField(max_length=11)
        image=models.ImageField(upload_to='products/')

class Cart1(models.Model):
        customer_Id=models.ForeignKey(Customer, on_delete=models.CASCADE)
        product_Id=models.ForeignKey(Product, on_delete=models.CASCADE)
        address=models.CharField(max_length=100)
        amount=models.FloatField()



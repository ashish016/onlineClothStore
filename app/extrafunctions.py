from random import randint
from app.models import Customer,Product
from django.shortcuts import render
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def showTrendings():
    data = Product.objects.filter(product_Id='XY12')

    return ( data )
from django.contrib import admin

# Register your models here.
from app.models import Customer,Product,Cart1,CustomAuth
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Cart1)
admin.site.register(CustomAuth)

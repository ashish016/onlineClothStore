from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control

from app.models import Customer,Product
from app.extrafunctions import random_with_N_digits,showTrendings


def index(request):
        result=showTrendings()
        for r in result:
            print(r.product_Name)
        return render(request, "index.html",{'res':result})
def login(request):
        return render(request,'login.html')

def signin(request):
        username=request.POST.get("username")
        print(type(username))
        password=request.POST.get("password")
        print(password)
        logindata=Customer.objects.get(email=username)
        print(logindata.password)
        print(type(logindata.password))
        #print(usernamedata)
        #passworddata = Student.objects.get(password=password)
        #print(passworddata.password)
        request.session['customer_Id'] = logindata.getPrimaryKey()
        res = request.session['customer_Id']
        print(logindata.customer_Id)
        print(res)
        if logindata.type=="Seller":
            if logindata.password == password:
                return render(request,'admin.html' )
            else:
                return render(request, 'error.html')

        if logindata.password==password:
                        return render(request,'dashboard.html' ,{"firstname":logindata.first_Name})
        else:
                        return  render(request,'error.html')
def signup(request):
    print("Yes i am there")
    cid=random_with_N_digits(10)
    fname = request.POST.get("first_name")
    lname = request.POST.get("last_name")
    email = request.POST.get("email")
    pwd = request.POST.get("password")
    typ=request.POST.get("type")
    R1=Customer(customer_Id=cid,first_Name=fname,last_Name=lname,email=email,password=pwd,type=typ)
    R1.save()
    #return HttpResponseRedirect ("Successfully Created").render(request,'dashboard.html' ,{"firstname":fname})
    return HttpResponse("Successfully Created")

def register(request):
    return render(request, 'register.html')

def add_Products(request):
    return render(request,'addproduct.html')

def add_Product(request):
    print("I am here")
    pid=request.POST.get("product_Id")
    print(pid)
    pname=request.POST.get("product_Name")
    print(pname)
    image=request.FILES.get("image")
    pquantity=request.POST.get("product_Quantity")
    pprice=request.POST.get("product_Price")
    custid=request.session['customer_Id']
    print(custid)
    product=Product(product_Id=pid,product_Name=pname,product_Price=pprice,product_Quantity=pquantity,image=image,upload_Id=custid)
    product.save()
    return HttpResponse("Successfully Added")

def view_My_Products(request):
    custid = request.session['customer_Id']
    data=Product.objects.filter(upload_Id=custid)
    args={}
    args['product_list']=data
    for test in data:
        print(test.product_Name)

    return render(request,'myproducts.html',args)


def ajaxdata(request):
    data = request.GET["q"]

    result = Product.objects.filter(upload_Id=data)

    return render(request,"myproducts.html",{'res':result})

def editajaxdata(request):
    data = request.GET["q"]
    print("I am here only ")
    print(data)
    result = Product.objects.filter(product_Id=data)
    for test in result:
        print(test.product_Name)
    return render(request,"editproduct.html",{'res':result})


def logout(request):
    del request.session['customer_Id']
    print('Session Deleted')

    @cache_control(no_cache=True, must_revalidate=True)
    def func():
        # some code
        return
    return render(request,'index.html')
from multiprocessing import context
from django.shortcuts import render
from .models import *
# Create your views here.



def csutomers(request):
    customers = Customer.objects.all()
    context = {
        'customers':customers
    }
    return render(request, 'home.html',context=context)

def categories(request):
    categories = Category.objects.all()
    context = {
        'categories':categories
    }
    return render(request, 'home.html',context=context)


def products(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request, 'home.html',context=context)

def invoices(request):
    invoices = Invioce.objects.all()
    context = {
        'invoices':invoices
    }
    return render(request, 'home.html',context=context)
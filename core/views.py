from multiprocessing import context
import re
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import *
# Create your views here.



def home(request):
    products = Product.objects.all()
    context = {'title':'صفحة البيع',
    'products':products}
    return render(request, 'core/index.html',context=context)

def csutomers(request):
    customers = Customer.objects.all()
    context = {
        'customers':customers
    }
    return render(request, 'home.html',context=context)

def categories(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        if request.POST.get('type') == 'add':
            category_name = request.POST.get('category_name')
            try:
                category = Category.objects.create(name=category_name)
                category.save()
                return redirect('/')
            except Exception as e:
                return JsonResponse({'error':str(e)})
        if request.POST.get('type') == 'edit':
            category_name = request.POST.get('edit_category_name')
            category = Category.objects.get(id=request.POST.get('category_id'))
            category.name = category_name
            category.save()
            return redirect('/')
        if request.POST.get('type') == 'delete':
            category = Category.objects.get(id=request.POST.get('category_id'))
            category.delete()
            return redirect('/')
    else:
        if request.GET.get('type') == 'get_data':
            category = Category.objects.get(id=request.GET.get('category_id'))
            return JsonResponse({'category_name':category.name})
        if request.GET.get('search'):
            categories = categories.filter(name__icontains=request.GET.get('search'))
    categories_pages = Paginator(categories, 10)
    current_page = request.GET.get('page') if request.GET.get('page') else 1
    categories = categories_pages.get_page(current_page)
    context = {
            'title':'الفئات',
            'categories':categories,
            'pages': str(categories_pages.num_pages),
            'current_page': str(current_page),
        }
    return render(request, 'core/categories.html',context=context)


def products(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    if request.method == 'POST':
        if request.POST.get('type') == 'add':
            try:
                product_name = request.POST.get('name')
                product_price = request.POST.get('price')
                product_category = request.POST.get('category')
                product_size = request.POST.get('size')
                product = Product(name=product_name,price=product_price,category=Category.objects.get(id=product_category),size=product_size)
                if product:
                    product.save()
                return redirect('/')
            except Exception as e:
                return JsonResponse({'error':str(e)})
        if request.POST.get('type') == 'delete':
            product = Product.objects.get(id=request.POST.get('product_id'))
            product.delete()
            return redirect('/')
    else:
        if request.GET.get('type') == 'get_data':
            product = Product.objects.get(id=request.GET.get('category_id'))
            return JsonResponse({'category_name':product.name})
        if request.GET.get('search'):
            categories = categories.filter(name__icontains=request.GET.get('search'))
    products_pages = Paginator(products, 10)
    current_page = request.GET.get('page') if request.GET.get('page') else 1
    products = products_pages.get_page(current_page)
    context = {
        'title':'الأصناف',
        'products':products,
        'categories':categories,
        'pages': str(products_pages.num_pages),
        'current_page': str(current_page),
    }
    return render(request, 'core/products.html',context=context)

def invoices(request):
    invoices = Invioce.objects.all()
    context = {
        'invoices':invoices
    }
    return render(request, 'home.html',context=context)
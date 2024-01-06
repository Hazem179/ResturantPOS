from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import *
# Create your views here.



def home(request):
    return render(request, 'core/index.html')

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
        context = {
            'title':'الفئات',
            'categories':categories
        }
        return render(request, 'core/categories.html',context=context)


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
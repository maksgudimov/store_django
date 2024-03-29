from django.shortcuts import render , HttpResponse
from .models import ProductCategory,Product
#функции = контроллеры = вьюхи

def index(request):
    context = {
        'title': 'Store',
    }
    return render(request,'products/index.html',context)

def products(request):
    context = {
        'title' : 'Store - Каталог',
        'products' : Product.objects.all(),
        'categories' : ProductCategory.objects.all(),
    }
    return render(request,'products/products.html',context)
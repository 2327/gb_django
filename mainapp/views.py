import json
from django.shortcuts import render
from .models import Categories
from .models import Products


def main(request):
    title = 'главная'
    content = {'title': title}
    return render(request, 'mainapp/index.html', content)


def products(request, name=''):
#    with open('categories.json') as f:
#        categories = json.load(f)["categories"]
    categories = Categories.objects.all()[:6]
    products = Products.objects.all()
#    with open('product_description.json') as f:
#        product = json.load(f)

    content = {
        'title': 'Каталог',
        'categories': categories,
        'products': products
    }

    return render(request, 'mainapp/products.html', content)
    

def product(request, name=''):
    categories = Categories.objects.all()[:6]
    products = Products.objects.all()

    content = {
        'title': 'Каталог',
        'categories': categories,
        'product': product
    }

    return render(request, 'mainapp/products.html', content)


def contact(request):
    return render(request, 'mainapp/contact.html')

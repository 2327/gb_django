import json
from django.shortcuts import render


def main(request):
    return render(request, 'mainapp/index.html')


def products(request, name=''):
    with open('categories.json') as f:
        categories = json.load(f)["categories"]

    with open('product_description.json') as f1:
        product = json.load(f1)

    content = {
        'title': 'Каталог',
        'categories': categories,
        'product': product
    }

    return render(request, 'mainapp/products.html', content )
    


def contact(request):
    return render(request, 'mainapp/contact.html')

# Create your views here.

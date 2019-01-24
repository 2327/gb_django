import json
from django.shortcuts import render


def main(request):
    return render(request, 'mainapp/index.html')


def products(request, name=''):
    with open('links_menu.json') as f:
        links_menu = json.load(f)["links_menu"]

    content = {
        'title': 'Каталог',
        'links_menu': links_menu,
        'same_products': 'Пока незнаю'
    }

    return render(request, 'mainapp/products.html', content )
    


def contact(request):
    return render(request, 'mainapp/contact.html')

# Create your views here.

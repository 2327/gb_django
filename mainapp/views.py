import json
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Categories
from .models import Products
from basketapp.models import Basket



def main(request):
    title = 'главная'
    content = {'title': title}
    return render(request, 'mainapp/index.html', content)


#def products(request, name=''):
##    with open('categories.json') as f:
##        categories = json.load(f)["categories"]
#    categories = Categories.objects.all()[:6]
#    products = Products.objects.all()
##    with open('product_description.json') as f:
##        product = json.load(f)
#
#    content = {
#        'title': 'Каталог',
#        'categories': categories,
#        'products': products
#    }
#
#    return render(request, 'mainapp/products.html', content)
    
def products(request, pk=None):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    title = 'продукты'
    links_menu = Categories.objects.all()

    if pk is not None:
        if pk == 0:
            products = Products.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(Categories, pk=pk)
            products = Products.objects.filter(category__pk=pk).order_by('price')

        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products,
            'basket': basket,
        }

        return render(request, 'mainapp/products_list.html', content)

    same_products = Products.objects.all()[3:5]

    content = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products
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

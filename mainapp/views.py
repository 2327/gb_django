import json
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Categories
from .models import Products
from basketapp.models import Basket
import random


def main(request):
    title = 'главная'
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    content = {
        'title': title,
        'basket': basket,
        }
    return render(request, 'mainapp/index.html', content)


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    products = Products.objects.all()

    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Products.objects.filter(category=hot_product.category). \
                        exclude(pk=hot_product.pk)[:3]

    return same_products


def products(request, pk=None):
    title = 'продукты'
    links_menu = Categories.objects.all()
    basket = get_basket(request.user)

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

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    content = {
        'title': title,
        'links_menu': links_menu,
        'hot_product': hot_product,
        'same_products': same_products,
        'basket': basket,
    }

    return render(request, 'mainapp/products.html', content)


def product(request, pk):
    title = 'продукты'

    content = {
        'title': title,
        'links_menu': ProductCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
        'basket': get_basket(request.user),
    }

    return render(request, 'mainapp/product.html', content)


def contact(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    content = {
        'title': 'Контакты',
        'basket': basket,
    }

    return render(request, 'mainapp/contact.html', content)

from django.shortcuts import render


def main(request):
    return render(request, 'mainapp/index.html')


def products(request, name=''):
    links_menu = [
    {'href': 'products_all', 'name': 'все'},
    {'href': 'products_home', 'name': 'дом'},
    {'href': 'products_office', 'name': 'офис'},
    {'href': 'products_modern', 'name': 'модерн'},
    {'href': 'products_classic', 'name': 'классика'},]
    
    content = {
        'title': 'Каталог',
        'links_menu': links_menu,
        'same_products': 'Пока незнаю'
    }

    return render(request, 'mainapp/products.html', content )
    


def contact(request):
    return render(request, 'mainapp/contact.html')

# Create your views here.

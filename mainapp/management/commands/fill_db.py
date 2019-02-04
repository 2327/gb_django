from django.core.management.base import BaseCommand
from mainapp.models import Categories
from mainapp.models import Products
#from django.contrib.auth.models import User
from authapp.models import ShopUser

import json
import os

JSON_PATH = 'mainapp/json'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('categories')

        Categories.objects.all().delete()
        for category in categories['categories']:
            new_category = Categories(**category)
            new_category.save()

        products = load_from_json('product_description')

        Products.objects.all().delete()
        for product in products['products']:
            category_name = product["category"]
            _category = Categories.objects.get(name=category_name)
            product['category'] = _category
            new_product = Products(**product)
            new_product.save()

#        Создаем суперпользователя при помощи менеджера модели
#        super_user = User.objects.create_superuser('django', 'django@geekshop.local', 'geekbrains')
#        Создаем суперпользователя при помощи менеджера модели
        super_user = ShopUser.objects.create_superuser('django', 'django@geekshop.local', 'geekbrains', age=33)
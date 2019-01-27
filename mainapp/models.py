from django.db import models

# Create your models here.

class Categories(models.Model):
    name         = models.CharField(verbose_name='имя', max_length=64, unique=True)
    href         = models.CharField(verbose_name='ссылка', max_length=64, unique=True)
    description  = models.TextField(verbose_name='описание', max_length=64, blank=True)

    def __str__(self):
        return self.name

class Products(models.Model):
    name         = models.CharField(verbose_name='имя', max_length=64, unique=True)
    category     = models.ForeignKey(Categories, on_delete=models.CASCADE)
    href         = models.CharField(verbose_name='ссылка', max_length=64, unique=True)
    discount     = models.CharField(verbose_name='акция', max_length=64, blank=True)
    main_image   = models.CharField(verbose_name='Изображение', max_length=64, blank=True)
    images       = models.CharField(verbose_name='Дополнительные изображения', max_length=64, blank=True)
    images       = models.ImageField(upload_to='products_images', blank=True)
    price        = models.DecimalField(verbose_name='Цена продукта', max_digits=8, decimal_places=2, default=0)
    short_desc   = models.CharField(verbose_name='Краткое описание продукта', max_length=60, blank=True)
    description  = models.TextField(verbose_name='Описание', max_length=64, blank=True)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)

    def __str__(self):
        return f"{self.name} ({self.category.name})"


# TODO: метрическая система магазина, валюта
#class Products(models.Model):
#   "currency":"руб.",

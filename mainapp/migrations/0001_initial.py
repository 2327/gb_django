# Generated by Django 2.1.7 on 2019-02-16 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='имя')),
                ('href', models.CharField(max_length=64, unique=True, verbose_name='ссылка')),
                ('description', models.TextField(blank=True, max_length=64, verbose_name='описание')),
                ('is_active', models.CharField(blank=True, max_length=64, verbose_name='Активно')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='Имя')),
                ('discount', models.CharField(blank=True, max_length=64, verbose_name='Акция')),
                ('main_image', models.CharField(blank=True, max_length=64, verbose_name='Изображение')),
                ('images', models.CharField(blank=True, max_length=64, verbose_name='Дополнительные изображения')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Цена продукта')),
                ('short_desc', models.CharField(blank=True, max_length=60, verbose_name='Краткое описание продукта')),
                ('description', models.TextField(blank=True, max_length=64, verbose_name='Описание')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Количество на складе')),
                ('currency', models.CharField(default='руб.', max_length=4, verbose_name='Валюта')),
                ('is_active', models.CharField(blank=True, max_length=64, verbose_name='Активно')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Categories')),
            ],
        ),
    ]

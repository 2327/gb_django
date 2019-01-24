"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import mainapp.views as mainapp


urlpatterns = [
    path('', mainapp.main),
    path('index.html', mainapp.main, name=''),
    path('admin/', admin.site.urls),
    path('products/', mainapp.products, name='products'),
    path('products.html', mainapp.products, name='products'),
    path('products_all', mainapp.products, name='products_all'),
    path('products_home', mainapp.products, name='products_home'),
    path('products_office', mainapp.products, name='products_office'),
    path('products_modern', mainapp.products, name='products_modern'),
    path('products_classic', mainapp.products, name='products_classic'),
    path('products_<str:name>', mainapp.products, name='products_<str:name>'),
    path('contact/', mainapp.contact, name='contact'),
    path('contact.html', mainapp.contact, name='contact')
]    


#from django.urls import path
#import mainapp.views as mainapp
#
#app_name = 'mainapp'
#
#urlpatterns = [
#    path('', mainapp.products, name='index'),
#    path('<int:pk>/', mainapp.products, name='category'),
#    path('products/', mainapp.products, name='products'),
#    path('products.html', mainapp.products),
#    path('product_<str:name>', mainapp.products, name='product'),
#
from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
#   path('', mainapp.products, name='index'),
#   path('<int:pk>/', mainapp.products, name='category'),
    path('', mainapp.products, name='index'),
#    path('/', mainapp.products, name='index'),
    path('product_<str:name>', mainapp.products, name='product'),
    path('category/<int:pk>/', mainapp.products, name='category'),
]
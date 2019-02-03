from django.urls import path

import basketapp.views as basketapp

app_name = 'basketapp'

urlpatterns = [
    path('', basketapp.basket, name='view'),
    path('add/<int:id>/', basketapp.basket_add, name='add'),
    path('remove/<int:id>)/', basketapp.basket_remove, name='remove'),
]
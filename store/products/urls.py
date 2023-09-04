from django.urls import path, include
from django.conf import settings
from products.views import index,products

app_name = 'products'

urlpatterns = [
    path('',products,name='index')
]



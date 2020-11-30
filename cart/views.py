from django.shortcuts import render
from django.views import generic

from .models import Product

# Create your views here.


class ProductListView(generic.ListView):
    template_name = 'cart/product_list.html'
    queryset = Product.objects.all()

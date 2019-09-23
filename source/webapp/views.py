from django.shortcuts import render
from webapp.models import Product

# Create your views here.


def list_product(request, *args, **kwargs):
    products = Product.objects.filter()
    return render(request, 'index.html', context={
        'products': products
    })


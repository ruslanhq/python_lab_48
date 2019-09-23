from django.shortcuts import render, get_object_or_404
from webapp.models import Product

# Create your views here.


def list_product(request, *args, **kwargs):
    products = Product.objects.order_by('category', 'name').filter(count__gt=0)
    return render(request, 'index.html', context={
        'products': products
    })


def product_view(request, pk):
    products = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', context={
        'products': products
    })


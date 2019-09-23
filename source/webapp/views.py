from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Product
from webapp.forms import ProductForm

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


def product_create(request, *args, **kwargs):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'create.html', context={
            'form': form
        })
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            products = Product.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                category=form.cleaned_data['category'],
                count=form.cleaned_data['count'],
                price=form.cleaned_data['price']
            )
            return redirect('index')
        else:
            return render(request, 'create.html', context={
                'form': form
            })


def product_update(request, pk):
    products = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        form = ProductForm(data={
            'name': products.name,
            'description': products.description,
            'category': products.category,
            'count': products.count,
            'price': products.price
        })
        return render(request, 'update.html', context={
            'form': form,
            'products': products
        })
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            products.name= form.cleaned_data['name']
            products.description= form.cleaned_data['description']
            products.category= form.cleaned_data['category']
            products.count= form.cleaned_data['count']
            products.price= form.cleaned_data['price']
            products.save()
            return redirect('index')
        else:
            return render(request, 'update.html', context={
                'form': form,
                'products': products
            })


def product_delete(request, pk):
    products = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', {
            'products': products
        })
    elif request.method == 'POST':
        products.delete()
        return redirect('index')

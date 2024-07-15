from django.shortcuts import render, get_object_or_404
from .models import Products

# Create your views here.

def homepage(request):
    return render(request, 'products/index.html')


def products_listings(request):
    products = Products.objects.all()
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if min_price and max_price:
        products = products.filter(price__gte=min_price, price__lte=max_price)

    return render(request, 'products/products_listings.html', {'products': products})
 

def product_details(request, product_id):
    products = get_object_or_404(Products, pk=product_id)
    return render(request, 'products/product_details.html', {'products': products})



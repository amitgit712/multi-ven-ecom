from django.shortcuts import render, get_object_or_404
from products.models import Product


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    context = {
        'product': product
    }
    return render(request, 'products/product_detail.html', context)

from django.shortcuts import render

from products.models import Product


def homepage(request):
    recent_products = Product.objects.all().order_by('-id')[:6]
    context = {
        'recent_products': recent_products
    }
    return render(request, 'core/homepage.html', context)

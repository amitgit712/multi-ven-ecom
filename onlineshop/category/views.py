from django.shortcuts import get_object_or_404, render

from products.models import Product

from .models import ProductCategory


def product_categories(request):
    return {
        'product_categories': ProductCategory.objects.filter(active=True)
    }


def prod_category_wise(request, slug):
    category = get_object_or_404(
        ProductCategory, slug=slug, active=True
    )
    product = Product.objects.filter(
        category=category, active=True, in_stock=True
    )
    context = {
        'product': product
    }
    return render(request, 'category/prod_category_detail.html', context)

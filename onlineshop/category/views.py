# from django.shortcuts import render

from .models import ProductCategory


def product_categories(request):
    return {
        'product_categories': ProductCategory.objects.filter(active=True)
    }

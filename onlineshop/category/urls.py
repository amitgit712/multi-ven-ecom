from django.urls import path

from . import views

app_name = 'category'

urlpatterns = [
    path(
        'product-category/<slug>/',
        views.prod_category_wise,
        name='prod_category_wise'
    ),
]

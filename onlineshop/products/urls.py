from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('product/<slug>/', views.product_detail, name="product_detail")
]

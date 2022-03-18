from django.urls import path

from . import views

app_name = 'vendor'

urlpatterns = [
    path('become-vendor/', views.become_vendor, name='becomeVendor'),
]

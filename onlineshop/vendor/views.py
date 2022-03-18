from django.shortcuts import render


def become_vendor(request):
    return render(request, 'vendor/become_vendor.html')

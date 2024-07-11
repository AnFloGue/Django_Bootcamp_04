from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def home_view(request):
    return render(request, 'home.html', {})


def product_detail_view(request, *args, **kwargs):
    obj = Product.objects.get(id=1)
    return HttpResponse(f"Product id {obj.id}")
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from django.http import JsonResponse


def home_view(request):
    return render(request, 'home.html', {})


def product_detail_view(request, pk):
    try:
        obj = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return HttpResponse("Product not found")
    return HttpResponse(f"Product id {obj.id}")


def product_api_detail_view(request, pk):
    try:
        obj = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return JsonResponse({"message": "Not found"}, status=404)
    return JsonResponse({"id": obj.id})
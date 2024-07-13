from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Product
from django.http import JsonResponse
from .forms import ProductModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


def info_request_any_view(request, *args, **kwargs):
    print(f"POST Dict:{request.POST}")
    print(f"GET Dict:{request.GET}")
    
    print(f"method, POST:{request.method == 'POST'}")
    print(f"method, GET:{request.method == 'GET'}")


def home_view(request):
    info_request_any_view(request)
    
    context = {
        "name": "Antonio",
        "age": 55
    }
    return render(request, 'home.html', context)


@staff_member_required
def product_create_view(request, *args, **kwargs):
    form = ProductModelForm(request.POST or None)
    
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = ProductModelForm()
    
    return render(request, "forms.html", {"form": form})


def product_detail_view(request, pk):
    info_request_any_view(request)
    try:
        obj = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return HttpResponse("Product not found")
    return render(request, "products/detail.html", {"object": obj})


def product_list_view(request):
    info_request_any_view(request)
    qs = Product.objects.all()
    context = {
        "object_list": qs
    }
    return render(request, "products/list.html", context)


def product_api_detail_view(request, pk):
    info_request_any_view(request)
    try:
        obj = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return JsonResponse({"message": "Not found"}, status=404)
    return JsonResponse({"id": obj.id})


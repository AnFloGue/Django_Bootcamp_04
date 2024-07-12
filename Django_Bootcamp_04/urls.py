from django.contrib import admin
from django.urls import path

from products.views import (
    home_view,
    product_create_view,
    product_detail_view,
    product_list_view,
    product_api_detail_view
)

urlpatterns = [
    path('', home_view),
    path('search/', home_view),
    path('products/<int:pk>/', product_detail_view),
    path('products/', product_list_view),
    path('products/create/', product_create_view),
    path('products/api/<int:pk>/', product_api_detail_view),
    path('admin/', admin.site.urls),
    path('products/detail/<int:pk>/', product_detail_view, name='product-detail'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.product_search, name='product-search'),
    path('product/create/', views.product_create, name='product-create'),
]

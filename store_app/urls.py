from django.contrib import admin
from django.urls import path
from . import views
from .views import ProductsView, ManufacturersView, ProductCreateView

urlpatterns = [
    path('', views.index),
    path('products', ProductsView.as_view(), name='products'),
    path('manufacturers', ManufacturersView.as_view(), name='manufacturers'),
    path('products/<int:pk>/', ProductsView.as_view(), name='product'),
    path('product', ProductCreateView.as_view(), name='product'),
    
]
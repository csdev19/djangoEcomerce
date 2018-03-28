from django.contrib import admin
from django.urls import path
from products.views import HomeView, ProductDetailView


urlpatterns = [
    path('', HomeView.as_view(), name="home") ,
    path('products/<slug:slug>', ProductDetailView.as_view(), name="detail") ,
]

from django.contrib import admin
from django.urls import path
from products.views import HomeView, ProductDetailView, ProductBuyView


urlpatterns = [
    path('', HomeView.as_view(), name="home") ,
    path('products/<slug:slug>/', ProductDetailView.as_view(), name="detail") ,
    path('products/<slug:slug>/buy/', ProductBuyView.as_view(), name="buy") ,
]

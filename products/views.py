from django.shortcuts import render
from django.views.generic import TemplateView
from products.models import Product


# Create your views here.
# def test (request):
#     return render(request, "products/test.html")


class HomeView (TemplateView):
    template_name = 'products/home.html'  

    def get_context_data(self, *ärgs,**kwargs):
        products = Product.objects.all()
        return {'products':products}
    

from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from products.models import Product, LogBuy
from comments.forms import CommentForm
from django.conf import settings
import stripe

# Create your views here.
# def test (request):
#     return render(request, "products/test.html")


class HomeView (TemplateView):
    template_name = 'products/home.html'  

    def get_context_data(self, *ärgs,**kwargs):
        products = Product.objects.all()
        return {'products':products}
    
class ProductDetailView (DetailView):
    model = Product
    # template_name = 'products/product_detail.html '
    # no es necesario porque un detailview busca un archivo con el sufijo _detail 

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        comment_form = CommentForm()
        context['comment_form'] = comment_form
        return context


class ProductBuyView(DetailView):
    model = Product
    template_name = 'products/buy.html'

    def post(self, request, *args, **kwargs):
        stripe.api_key = settings.STRIPE_API_KEY
        token = request.POST['stripeToken']
        product = self.get_object()
        error_message =  None

        try:
            charge = stripe.Charge.create(
                amount=product.price,
                currency='usd',
                description='cobro por {}'.format(product.title),
                statement_descriptor='cobro es obligatorio',
                source=token
            )

        except stripe.error.CardError as e:
            body= e.json_body
            err = body['error']
            error_message = err['message']

        except stripe.error.StripeError as e:
            error_message = 'cant process your payment please try again later'

        if error_message:
            return render(request, 'products/failed.html', {'error_message':error_message, 'product':product})

        buyer = None

        if request.user.is_authenticated:
            buyer = request.user

        LogBuy.objects.create(product=product, user=buyer)

        return render(request, 'products/success.html', {'debug_info':charge, 'product':product})
    
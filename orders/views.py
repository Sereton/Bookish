import stripe
from django.conf import settings
from django.contrib.auth.models import Permission
from django.views.generic.base import TemplateView
from django.shortcuts import render

# Create your views here.

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

class OrdersPageView(TemplateView):
    template_name ='orders/purchase.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context

def charge(request):
    permission = Permission.objects.get(codename='premium')
    u = request.user
    
    if request.method == 'POST':
        charge = stripe.Charge.create(amount=3500,currency='usd',description='Purchase All Books',source=request.POST['stripeToken'])
        u.user_permissions.add(permission)

    return render(request, 'orders/charge.html')
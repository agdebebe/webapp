from django.shortcuts import render
from cart.models import Order, Cart
from . models import BillingForm, BillingAddress
from django.views.generic.base import TemplateView

# Create your views here.
def checkout(request):

	# Checkout view
	form = BillingForm

	order_qs = Order.objects.filter(user= request.user, ordered=False)
	order_items = order_qs[0].orderitems.all()
	order_total = order_qs[0].get_totals()
	context = {"form": form, "order_items": order_items, "order_total": order_total}

	return render(request, 'checkout/index.html', context)

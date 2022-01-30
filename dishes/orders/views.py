from django.shortcuts import render, redirect, get_object_or_404
from catalog.models import Product
from .form import OrderCreateForm
from decimal import Decimal
from cart.cart import Cart

from django.conf import settings
import weasyprint
from django.contrib.admin.views.decorators import staff_member_required 
from .models import Order, OrderItem
from django.template.loader import render_to_string
from django.http import HttpResponse
from .tasks import order_created
from django.core.mail import send_mail
# Create your views here.


def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'admin/orders/detail.html', {'order': order})

def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    html = render_to_string('admin/orders/pdf.html', {'order': order})
    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = f'filename=order_{order.id}.pdf'
    weasyprint.HTML(string=html).write_pdf(response)
    return response

# def step_1(request):
#     return render(request, )


def orderTest(request):
    cart = Cart(request)
    

    if request.method == 'POST':
        order_form = OrderCreateForm(request.POST)
        error = ''
        
        if order_form.is_valid():
            order = order_form.save()
           

            
            for i in cart:                   
                OrderItem.objects.create(order=order,product=i['product'],quantity=i['quantility'])
            cart.clear()
            try:
                order_created.delay(order.id)
                return render(request,'cart/shop-cart.html' )
            except:
                return "error"               
    else:
        error = 'error'
        order_form = OrderCreateForm()
    return render(request,'cart/shop-checkout.html',{'error':error, 'cart': cart,'order_form': order_form,   })




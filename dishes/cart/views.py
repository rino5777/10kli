from .cart import Cart

from catalog.models import Product, Category
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_POST
from django.urls import reverse

from .forms import Add_to_form, Cart_add_remove
from decimal import Decimal
from django.conf import settings
from orders.form import OrderCreateForm
from orders.models import OrderItem
from django.contrib import messages
from django.core.mail import send_mail
from orders.models import Order
from orders.tasks import order_created
from orders.views import admin_order_pdf

# @require_POST
# def cart_add(request, product_id):
#     cart = Cart(request)
#     product = get_object_or_404(Product, id = product_id )
#     form  = Add_to_form(request.POST)

#     if form.is_valid():
#         clean = form.cleaned_data
#         cart.add(product = product, quantility = clean['quantility'], updateq = clean['update'] )
#     return redirect('cart:cart')
        


# def cart_remove(request, product_id ):
#     cart = Cart(request)
#     product = get_object_or_404(Product, id = product_id )
#     cart.remove(product)
#     return redirect('cart:cart')



# def scart(request):
#     cart = Cart(request)
    

#     return render(request, 'cart/cart1.html', {'cart': cart })






@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id = product_id )
    form  = Add_to_form(request.POST)

    if form.is_valid():
        clean = form.cleaned_data
        cart.add(product = product, quantility = clean['quantility'], updateq = clean['update'] )
        messages.success(request, 'Товар добавлен в корзину !')
    #return render(request, ('catalog:product'))    
    return redirect(reverse('cart:scart'))
        

def minus(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id = product_id )
    form  = Add_to_form(request.POST)

    if form.is_valid():
        clean = form.cleaned_data
        cart.minus_1_from_cart(product = product, quantility = clean['quantility'], updateq = clean['update'] )
        messages.success(request, 'Товар добавлен в корзину !')
    #return render(request, ('catalog:product'))    
    return redirect(reverse('cart:scart'))




def cart_remove(request, product_id ):
    cart = Cart(request)
    product = get_object_or_404(Product, id = product_id )
    
    cart.remove(product)
    return redirect('cart:scart')






def scart(request, ):
    error = ''
    form_order = OrderCreateForm()
    main_cat = Category.objects.all()
    cart = Cart(request)
    cart_form_2 = Add_to_form()
    cart_form_3 = Cart_add_remove()
    
    if request.method == 'POST':
        form_order = OrderCreateForm(request.POST)
       
        #send_mail(subject, message, settings.EMAIL_HOST_USER , ['10kli.israel@gmail.com'])
        if form_order.is_valid(): 
            order = form_order.save()
            #orderr = OrderItem.objects.get(id = product.id)
            for i in cart:
                    #i ['update_quantity_form'] = Add_to_form(initial={'quantity': i['quantity'], 'update': True}) 
                    #OrderItem.objects.create(order=order,product=i['product'], quantity=i['quantility'])
                    OrderItem.objects.create(order=order,product=i['product'], quantity=i['quantility'])


            
            subject = f' new order {order.id} '
            message = f'ЗАКАЗ ОТ  {order.first_name},{order.last_name} ( НАЗВАНИЕ ФИРМЫ  {order.company_name} )  \n\n' \
                        f' почта {order.email}.\n' \
                        f' ТЕЛЕФОН {order.telephone}.\n' \
                        f' АДРЕСС: {order.city} {order.address}.\n' \
                        f'ТЕКСТ: {order.note}.\n' 
            
            
            send_mail(subject, message, settings.EMAIL_HOST_USER , ['hhharbot@gmail.com'])
            #order_created.delay(order.id)
            cart.clear()
            return render(request,'cart/shop-cart.html',{'order': order} )
        else:
           
            error = 'ERROR form_order  NOT valid'
    else:
        #messages.add_message(request, messages.INFO, 'Hello world.')
        form_order = OrderCreateForm()

    return render(request, 'cart/shop-checkout.html', {'error':error,'form_order': form_order,  'cart': cart, "cart_form_2":cart_form_2, main_cat:'main_cat' })






from django.http import request
from django.shortcuts import render, get_object_or_404, redirect
from catalog.models import Category, Product, Subcategory 
from .form import OrderCreateForm
from blog.models import Content
from .models import Adv
from django.conf import settings
from django.core.mail import send_mail

def index(request, category_slug = None):
    categoryes = Category.objects.all()
    content = Content.objects.all()
    words = get_object_or_404(Adv)
    category = None
    if  category_slug :
        category = get_object_or_404(Category, slug = category_slug )
     
   
    return render(request, 'home/home.html', {'elements': categoryes, 'category': category,  'content': content, 'words':words }, )




def about_us(request):
    words = get_object_or_404(Adv)
    return render(request, 'about_us/about-us.html', { 'words':words} )



def contact(request):
    words = get_object_or_404(Adv)
    error = ''
    if request.method == 'POST':
        order_form = OrderCreateForm(request.POST)
        if order_form.is_valid():
            order = order_form.save()
    
            subject = f' פנייה'
            message = f'  {order.first_name} לקוח \n\n' \
                        f'  {order.email} :מייל\n' \
                        f'  {order.telephone} :טלפון\n' \
                        f'  {order.address} :כתובת\n' \
                        f' {order.note} :טקסט\n' \
                        f'  מבקש ליצור קשר     \n' \
            
            send_mail(subject, message, settings.EMAIL_HOST_USER , ['10kli.israel@gmail.com'])
            #order_created.delay(order.id)
            

            
                        
            return render(request,'contact/contact-notification.html' )          
        else:
            error = 'error'
    order_form =  OrderCreateForm()
    return render(request,'contact/contact-us.html',{'order_form': order_form, 'error': error, 'words':words })


def search(request, subcategory_slug=None):
    if request.method == 'POST':
        searche = request.POST['searche']
        product = Product.objects.filter(name__contains = searche )
        subcategory = Subcategory.objects.filter(name__contains = searche)
        category = Category.objects.all()
        if subcategory_slug:
            requested_subcategory = get_object_or_404(Subcategory, slug=subcategory_slug )
            product = Product.objects.filter( subcategory=requested_subcategory )
            subcategory = requested_subcategory

        return render(request,'search/search_page.html',
            {'searche':searche, 'product':product, 'subcategory':subcategory, 'category':category,  'product': product })
    else:
        return render(request, 'search/search_page.html', {})
from django.shortcuts import get_object_or_404
from django.http import request
from django.shortcuts import render
from .models import Category, Subcategory,  Product
from cart.forms import Add_to_form, Cart_add_remove
from main.models import Adv


def catalog(request, category_slug = None):
    main_cat = Category.objects.all()
    subcategories = Subcategory.objects.filter()

    category = None
    words = get_object_or_404(Adv)
    if  category_slug :
        category = get_object_or_404(Category, slug = category_slug )
        subcategories = subcategories.filter(category = category)
   
    return render(request, 'catalog/catalog.html', {'elements_main': main_cat, 'subcategories': subcategories, 'categories': category, 'words': words  } )


def product_detail(request, category_slug, subcategory_slug=None):
    subcategory = Subcategory.objects.all(  )
    requested_subcategory = None
    product = Product.objects.all()
    main_cat = Category.objects.all()
    if subcategory_slug:
        requested_category = get_object_or_404(Category, slug=category_slug)
        requested_subcategory = get_object_or_404(Subcategory, slug=subcategory_slug )
        product = Product.objects.filter( subcategory=requested_subcategory )

    return render(request,'catalog/product_detail.html', {'elements_main': main_cat, 'product': product, 'subcategory':subcategory, 'requested_subcategory': requested_subcategory})

def product(request, id, slug):
    all_categoryes = get_object_or_404(Product, id = id, slug = slug  )
    cart_form = Cart_add_remove()
    return render(request, 'catalog/product_page1.html', {'elem': all_categoryes, 'cart_form':cart_form } )
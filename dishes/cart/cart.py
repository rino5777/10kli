from django.conf import settings 
from catalog.models import Product
from decimal import Decimal
from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ObjectDoesNotExist

# class Cart(object):



#     def __init__(self, request):
#         self.session = request.session
#         cart = self.session.get(settings.CART_SESSION_ID)  #как вышлядит  cart? 
#         if not cart:
#            cart = self.session[settings.CART_SESSION_ID] = {}
#         self.cart = cart
        


		
#     def add(self, product, quantility = 1, updateq=False):
# 	    product_id = str(product.id)
# 	    if product_id not in self.cart:
# 		    self.cart[product_id ] = {'quantility': 0 }  #[ 'q':{'quantility': 0, 'price': str(product.price)} ]
# 	    if updateq:
# 		    self.cart[product_id]['quantility'] = quantility   #[ 'q':{'quantility': (quantility = 1), 'price': str(product.price)} ]
# 	    else:
# 		    self.cart[product_id]['quantility'] += quantility   #[ 'q':{'quantility': += (quantility = 1), 'price': str(product.price)} ]
# 	    self.save() 
		
#     def save(self):
# 	    self.session[settings.CART_SESSION_ID]  = self.cart
# 	    self.session.modifed = True

  

#     def __iter__(self):
		 
# 	    all_productId = self.cart.keys()
# 	    products = Product.objects.filter( id__in = all_productId )
# 	    for product in products:
# 		    self.cart[ str(product.id) ]['product'] = product

# 	    for i in self.cart.values():
# 		    yield i
	

	    

    

    

    # def clear(self):
	#     del self.session[settings.CART_SESSION_ID]
	#     self.session.modified = True


   
class Cart(object):



    def __init__(self, request):
        self.session = request.session
		
        cart = self.session.get(settings.CART_SESSION_ID)  #как вышлядит  cart? 
        if not cart:
           
           cart = self.session[settings.CART_SESSION_ID] = {}
		   

		
        self.cart = cart
        


		
    def add(self, product, quantility = 1, updateq=False):
        product_id = str(product.id)
        
        if product_id not in self.cart:
            self.cart[product_id ] = {'quantility': 0, }  #[ 'q':{'quantility': 0, 'price': str(product.price)} ]
        if updateq:
            self.cart[product_id]['quantility'] = quantility   #[ 'q':{'quantility': (quantility = 1), 'price': str(product.price)} ]
        else:
            self.cart[product_id]['quantility'] += quantility   #[ 'q':{'quantility': += (quantility = 1), 'price': str(product.price)} ]
        self.save()

        if self.cart[product_id]['quantility']  == 0:
            del self.cart[product_id]
            self.save()

            
        if product_id in self.cart:
            if self.cart[product_id]['quantility']   == 0:
                del self.cart[product_id]
                  
                self.save()

            if self.cart[product_id]['quantility']  < 0:
                del self.cart[product_id]
                
                self.save()
                  
            
        # if product_id in self.cart:
        #     if self.cart[product_id]['quantility'] -  quantility == 0:
        #          del self.cart[product_id]
        # if quantility == self.cart[product_id]['quantility']:
        #     del self.cart[product_id]
        #     self.save()


		
    def save(self):
	    self.session[settings.CART_SESSION_ID]  = self.cart
	    self.session.modifed = True

    def remove(self, product, quantility = 1 ):
	    #self.cart[product_id ] = {'quantility': 0, 'price': str(product.price)} 
        
        product_id = str(product.id)


        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
		 
	    all_productId = self.cart.keys()
	    products = Product.objects.filter( id__in = all_productId )
	    for product in products:
		    self.cart[ str(product.id) ]['product'] = product

	    for i in self.cart.values():
		   
		    yield i 

    def __len__(self):
	    return sum(i['quantility'] for i in self.cart.values() )

   

    def clear(self):
	    del self.session[settings.CART_SESSION_ID]
	    self.session.modified = True


    def remove_from_cart(self, product, quantility = 1 ):
	    #self.cart[product_id ] = {'quantility': 0, 'price': str(product.price)} 
        product_id = str(product.id)

        if  product_id in self.cart:
	        if self.cart[product_id]['quantility'] > 1:
            #del self.cart[product_id]
                 self.cart[product_id]['quantility'] -= 1
	        else:
	            del self.cart[product_id]
        	self.save()



    def minus_1_from_cart(self, product, quantility = 1, updateq=False):
	    product_id = str(product.id)
	    if product_id not in self.cart:
		    self.cart[product_id ] = {'quantility': 0, }  #[ 'q':{'quantility': 0, 'price': str(product.price)} ]
	    if updateq:
		    self.cart[product_id]['quantility'] = quantility   #[ 'q':{'quantility': (quantility = 1), 'price': str(product.price)} ]
	    else:
		    self.cart[product_id]['quantility'] -= quantility   #[ 'q':{'quantility': += (quantility = 1), 'price': str(product.price)} ]
	    self.save() 
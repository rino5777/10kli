from django.urls import path 
from . import views
from orders.views import orderTest
app_name = 'cart'


urlpatterns = [
    
    path('', views.scart, name='scart'),
    path('add/<product_id>/', views.cart_add, name='cart_add'),
    path('remove/<product_id>/', views.cart_remove, name='cart_remove'),
    path('minus/<product_id>/', views.minus, name='minus'),
]
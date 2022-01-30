from django.urls import path 
from . import views

app_name = 'catalog'


urlpatterns = [
    path('catalog', views.catalog, name = 'catalog' ),
    path('<slug:category_slug>', views.catalog, name = 'Subcategory' ),

    path('<slug:category_slug>/<slug:subcategory_slug>/',views.product_detail,name='product_detail'),
    path('<id>/<slug>', views.product, name = 'product' ),
]
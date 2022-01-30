from django.urls import path 
from . import views

app_name = 'main'


urlpatterns = [
    path('', views.index, name = 'main_page' ),
    path('about_us/', views.about_us, name = 'about_us' ),
    path('contact/', views.contact, name = 'contact' ),
    path('search/', views.search, name = 'search' ),
    

]
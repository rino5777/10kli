from django.urls import path 
from . import views

app_name = 'blog'


urlpatterns = [
    path('', views.posts_line, name = 'posts_line' ),

    path('f/<slug:slug>/', views.content, name = 'content' ),
    

]


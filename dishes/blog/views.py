from django.shortcuts import render, get_object_or_404
from .models import Content
# Create your views here.


def posts_line(request):
    post = Content.objects.all( )
    
    
    return render( request, 'blog/blog_main.html', {'post':post})

def content(request, slug = None):
    #content = Content.objects.all()
    if slug:
        content = get_object_or_404(Content, slug = slug )

    return render(request, 'blog/blog-single.html', { 'content': content })
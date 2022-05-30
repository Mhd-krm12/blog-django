from django.shortcuts import render, get_object_or_404, redirect
from matplotlib.style import context
from .models import Post

# posts=[]
def home(request):
    context={
        'title':Post,
        'posts':Post.objects.all()
    }
    return render(request, 'blog/index.html' , context)

def about(request):
    
    return render(request, 'blog/about.html' )


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context={
        'title':'title',
        'post':post,
    }

    return render(request, 'blog/detail.html',  context )

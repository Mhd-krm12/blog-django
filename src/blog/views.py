from django.shortcuts import render, get_object_or_404, redirect
from matplotlib.style import context
from .models import Post,Comment
from .forms import NewComment

# posts=[]
def home(request):
    context={
        'title':"Anasyfa",
        'posts':Post.objects.all()
    }
    return render(request, 'blog/index.html' , context)

def about(request):
    
    return render(request, 'blog/about.html' )


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.filter(active=True)

    # check before save data from comment form
    if request.method == 'POST':
        comment_form = NewComment(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            # Deprecated line to prevent form to post data when refresh a page
            comment_form = NewComment()
            return redirect('detail', post_id)
    else:
        comment_form = NewComment()

    context = {
        'title': post,
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, 'blog/detail.html', context)
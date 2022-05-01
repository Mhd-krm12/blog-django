from django.shortcuts import render
from matplotlib.style import context

posts=[
    {'title':'Birinci paylaşım',
    'content':'Birinici paylaşım içeriği',
    'post_date':'15-1-2019',
    'author':'ahmed Bey'
    },
    {'title':'İkinci paylaşım',
    'content':'Birinici paylaşım içeriği',
    'post_date':'15-2-2019',
    'author':'Efe Bey'
    },
    {'title':'Üçüncü paylaşım',
    'content':'Birinici paylaşım içeriği',
    'post_date':'15-3-2019',
    'author':'Ali Bey'
    },
    {'title':'Dörtüncü paylaşım',
    'content':'ikinci paylaşım içeriği',
    'post_date':'15-4-2019',
    'author':'Mehmet Bey'
    }

]
# Create your views here.
def home(request):
    context={
        'title':'Anasayfa',
        'posts':posts,
    }
    return render(request, 'blog/index.html' , context)



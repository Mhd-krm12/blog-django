from django.shortcuts import render
from matplotlib.style import context

posts=[
    {'title':'Birinci paylaşım',
    'content':'Birinici paylaşım içeriği .. Birinici paylaşım içeriği .. Birinici paylaşım içeriği .. Birinici paylaşım içeriği .. Birinici paylaşım içeriği .. Birinici paylaşım içeriği .. Birinici paylaşım içeriği .. Birinici paylaşım içeriği .. Birinici paylaşım içeriği .. Birinici paylaşım içeriği .. ',
    'post_date':'15-1-2019',
    'author':'ahmed Bey'
    },
    {'title':'İkinci paylaşım',
    'content':'İkinci paylaşım içeriği .. İkinci paylaşım içeriği .. İkinci paylaşım içeriği .. İkinci paylaşım içeriği .. İkinci paylaşım içeriği .. İkinci paylaşım içeriği .. İkinci paylaşım içeriği .. İkinci paylaşım içeriği .. İkinci paylaşım içeriği .. İkinci paylaşım içeriği .. ',
    'post_date':'15-2-2019',
    'author':'Efe Bey'
    },
    {'title':'Üçüncü paylaşım',
    'content':'üçünü paylaşım içeriği .. üçünü paylaşım içeriği .. üçünü paylaşım içeriği .. üçünü paylaşım içeriği .. üçünü paylaşım içeriği .. üçünü paylaşım içeriği .. üçünü paylaşım içeriği .. üçünü paylaşım içeriği .. üçünü paylaşım içeriği .. üçünü paylaşım içeriği ..',
    'post_date':'15-3-2019',
    'author':'Ali Bey'
    },
    {'title':'Dörtüncü paylaşım',
    'content':'Dörtüncü paylaşım içeriği ..  Dörtüncü paylaşım içeriği .. Dörtüncü paylaşım içeriği .. Dörtüncü paylaşım içeriği .. Dörtüncü paylaşım içeriği .. Dörtüncü paylaşım içeriği .. Dörtüncü paylaşım içeriği .. Dörtüncü paylaşım içeriği .. Dörtüncü paylaşım içeriği .. Dörtüncü paylaşım içeriği .. ',
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

def about(request):
    
    return render(request, 'blog/about.html' )



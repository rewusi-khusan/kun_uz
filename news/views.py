from django.shortcuts import render

from news.models import News


# Create your views here.

def index(request):
    news = News.objects.order_by('-published_time')
    context = {
        'news': news,
    }
    return render(request, 'index.html', context)



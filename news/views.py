from django.shortcuts import render
from news.models import News, Category


# Create your views here.

def index(request):
    news = News.objects.order_by('-published_time')[0:3]
    context = {
        'news': news,
    }
    return render(request, 'index.html', context)


def categories_view(request):
    categories = Category.objects.all()
    news = News.objects.all()
    context = {
        'categories': categories,
        'news': news,
    }
    return render(request, 'categori.html', context)


def category_detail(request, id):
    categories = Category.objects.all()
    news = News.objects.filter(category__id=id)
    context = {
        'categories': categories,
        'news': news,
    }
    return render(request, 'categori.html', context)

def yangilik_view(request, slug):
    new = News.objects.get(slug=slug)
    new.views_count += 1
    new.save()

    context = {
        'new': new,
    }
    return render(request, 'yangilik.html', context)


from django.shortcuts import render
from post.models import Category, News, Comment, Contact, Saved
from django.contrib.auth.models import User
# Create your views here.


# def get_home(request):
#     return render(request, 'index.html')

# def get_home(request):
#     categorys = Category.objects.all()
#     news_list = News.objects.order_by('-id')[:4]
#     return render(request, 'index.html', {'categorys': categorys,
#         'news_list': news_list})


def get_home(request):
    categories = Category.objects.all()
    first_news = []

    for cat in categories:
        post = News.objects.filter(category=cat).first()
        if post:
            first_news.append(post)

    return render(request, 'index.html', {
        'categories': categories,
        'first_news': first_news[-4:]
    })

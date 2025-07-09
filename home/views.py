from django.shortcuts import render
from post.models import Category, News, Comment, Contact, Saved
from django.contrib.auth.models import User
# Create your views here.


# def get_home(request):
#     return render(request, 'index.html')

def get_home(request):
    categorys = Category.objects.all()
    return render(request, 'index.html', {'categorys': categorys})
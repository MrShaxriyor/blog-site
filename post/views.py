from django.shortcuts import render
from .models import Category, News, Comment, Contact, Saved
from django.contrib.auth.models import User
# Create your views here.




# def category_list(request):
#     categorys = Category.objects.all()
#     return render(request, 'index.html', {'categorys': categorys})
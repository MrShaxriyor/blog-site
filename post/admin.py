from django.contrib import admin
from .models import *
# Register your models here.





class newsAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'created_at', 'updated_at', 'image']
    search_fields = ['title', 'content']
    list_filter = ['category', 'created_at']

class categoryad(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']

admin.site.register(News, newsAdmin)
admin.site.register(Category, categoryad)
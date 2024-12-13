from django.contrib import admin
from .models import Message, Article, News, Category

admin.site.register(Message)
admin.site.register(Article)
admin.site.register(News)
admin.site.register(Category)



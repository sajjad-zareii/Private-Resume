from django.shortcuts import render
from home.models import Message, Article, News


def home(request):
    articles = Article.objects.all()
    last_news = News.objects.all()
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        body = request.POST.get('body')
        Message.objects.create(name=name, email=email, body=body)
    return render(request, "home/home.html", {'articles': articles, 'last_news': last_news})

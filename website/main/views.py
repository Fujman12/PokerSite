from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Article
# Create your views here.

def index(request):
    context = dict()
    context['articles'] = Article.objects.all()
    return render(request, 'main/index.html', context)

def article(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404("Album does not exist!")
    context = dict()
    context['article'] = article
    return render(request, 'main/article.html', context)

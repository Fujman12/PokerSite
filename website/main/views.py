from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from .models import Article
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    context = dict()
    context['articles'] = Article.objects.all()
    return render(request, 'main/index.html', context)

@login_required
def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    context = dict()
    context['article'] = article
    return render(request, 'main/article.html', context)
    

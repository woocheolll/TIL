from symbol import arith_expr
from django.shortcuts import render, redirect

import accounts
from .models import Article
from .form import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk')
    context={
        'articles' : articles
    }
    return render(request,'articles/index.html',context)

# def new(request):
#     article_form = ArticleForm()
#     context = {
#         'article_form' : article_form
#     }
#     return render(request,'articles/new.html', context=context)

def create(request):
    if request.user.is_authenticated:
        if request.method== 'POST':
            article_form = ArticleForm(request.POST)
            if article_form.is_valid():
                article_form.save()
                return redirect('articles:index')
        else:
            article_form = ArticleForm()
        context = {
            'article_form' : article_form
        }
        return render(request,'articles/new.html', context=context)
    else:
        return redirect('accounts:login')

def detail(request,pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request,'articles/detail.html', context)

from django.contrib.auth.decorators import login_required
def update(request,pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:detail', article.pk)
    else:
        article_form = ArticleForm(instance=article)
    context = {
        'article_form' : article_form
    }
    return render(request,'articles/form.html', context)

def delete(request, pk):
    Article.objects.get(pk=pk).delete()
    return redirect('articles:index')
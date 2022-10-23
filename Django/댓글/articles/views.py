from symbol import arith_expr
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import accounts
from .models import Article, Comment
from .form import ArticleForm,CommentForm
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    articles = Article.objects.all().order_by('-pk')
    
    page = request.GET.get('page') #GET 방식으로 정보를 받아오는 데이터
    paginator = Paginator(articles, '6') #Paginator(분할될 객체, 페이지 당 담길 객체수)
    page_obj = paginator.get_page(page) #페이지 번호를 받아 해당 페이지를 리턴 get_page 권장
    context={    
        'articles' : articles,
        'page': page_obj
    }
    return render(request,'articles/index.html',context)


# def new(request):
#     article_form = ArticleForm()
#     context = {
#         'article_form' : article_form
#     }
#     return render(request,'articles/new.html', context=context)
@login_required
def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            # 로그인한 유저 => 작성자네!
            article.user = request.user 
            article.save()
            messages.success(request, '글 작성이 완료되었습니다.')
            return redirect('articles:index')
    else: 
        article_form = ArticleForm()
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/form.html', context=context)

def detail(request, pk):
    # 특정 글을 가져온다.
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    # template에 객체 전달
    context = {
        'article': article,
        'comments': article.comment_set.all(),
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)

@login_required
def update(request,pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            article_form = ArticleForm(request.POST, instance=article)
            if article_form.is_valid():
                article_form.save()
                messages.success(request, '글이 수정되었습니다.')
                return redirect('articles:detail', article.pk)
        else:
            article_form = ArticleForm(instance=article)
        context = {
            'article_form' : article_form
        }
        return render(request,'articles/form.html', context)
    else:
        # 작성자가 아닐 때
        # (1) 403 에러메시지를 던져버린다. 
        # from django.http import HttpResponseForbidden
        # return HttpResponseForbidden()
        # (2) flash message 활용!
        messages.warning(request, '작성자만 수정할 수 있습니다.')
        return redirect('articles:detail', article.pk)


def delete(request, pk):
    Article.objects.get(pk=pk).delete()
    return redirect('articles:index')

@login_required
def comment_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
    return redirect('articles:detail', article.pk)

def comments_delete(request,article_pk,comment_pk):
    comment=Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)


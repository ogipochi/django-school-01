from django.shortcuts import render
from .models import Article
from django.core.paginator import Paginator

def article_list(request):
    object_list = Article.objects.all()
    paginator = Paginator(object_list, 4)
    try:
        page = request.GET.get('page')
        articles = paginator.page(page)
    except:
        # ページが取得できなかった場合１ページ目に飛ばす
        page=1
        articles = paginator.page(page)
    return render(request,'blog/list.html',{
        'articles':articles,
        'page':page
        })

def article_detail(request,id):
    article = Article.objects.get(id=id)
    context = {
        'article':article
    }
    return render(request,'blog/detail.html',context)
from django.shortcuts import render
from .models import Article


def article_list(request):
    articles = Article.objects.all()
    return render(request,'blog/list.html',{'articles':articles})

def article_detail(request,id):
    article = Article.objects.get(id=id)
    context = {
        'article':article
    }
    return render(request,'blog/detail.html',context)
from django.shortcuts import render
from .models import Article
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def list_blog(request):
    list_article = Article.objects.all()
    context = {'list_article': list_article}
    return render(request, "blog.html", context)


@login_required(login_url='login')
def detail(request, id_article):
    article = Article.objects.get(id=id_article)
    context = {'article': article}
    return render(request, 'detail.html', context)

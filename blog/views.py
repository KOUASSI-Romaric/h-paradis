from django.shortcuts import render
from .models import Article


# Create your views here.
def list_blog(request):
    list_article = Article.objects.all()
    context = {'list_article': list_article}
    return render(request, "blog.html", context)


def detail(request, id_article):
    article = Article.objects.get(id=id_article)
    context = {'article': article}
    return render(request, 'detail.html', context)

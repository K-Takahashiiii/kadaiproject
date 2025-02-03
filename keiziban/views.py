from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Article
from .forms import ArticleForm
# from .forms import ArticleFormSet
# Create your views here.


def index(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles': articles})


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ArticleForm()
    return render(request, 'create.html', {'form': form})


def edit(request, article_id):
    article = get_object_or_404(Article, id = article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance = article)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'edit.html', {'form': form})


def delete(request, article_id):
    article = get_object_or_404(Article, id = article_id)
    if request.method =='POST':
        article.delete()
        return redirect('index')
    return render(request, 'delete.html', {'article': article})


# def add(request):
#     formset = ArticleFormSet(request.POST or None)
#     if request.method == 'POST' and formset.is_valid():
#         formset.save()
#         return redirect('index')

#     return render(request, 'create.html', {'formset': formset})
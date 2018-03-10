from django.shortcuts import render
from django.views import generic
from django.views import View
from .models import Article, TableOfContentsNode

# Create your views here.
class ArticleDetailView(generic.DetailView):
    model = Article


def article_table_of_contents(request):
    context = { 'root': TableOfContentsNode.objects.get(is_root=True) }
    return render(request, 'guide/article_list.html', context=context)

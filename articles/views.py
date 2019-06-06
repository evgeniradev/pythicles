from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils import timezone
from authors.models import Author
from .models import Article

import urllib


def index(request):
    articles, additional_params = apply_filters(request, load_articles())

    context = {
        'authors': load_authors(),
        'articles': apply_pagination(request, articles, per_page=10),
        'additional_params': additional_params,
        'displayed_pages_margin': 3
    }

    return render(request, 'articles/index.html', context)


def article(request, article_slug):
    context = {
        'authors': load_authors(),
        'article': get_object_or_404(Article, slug=article_slug)
    }

    return render(request, 'articles/article.html', context)


def apply_filters(request, articles):
    additional_params = []

    if 'author' in request.GET:
        author_slug = request.GET['author']
        articles = articles.filter(author__slug__iexact=author_slug)
        additional_params.append('&author=' + author_slug)

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        articles = articles.filter(
            Q(title__icontains=keywords) | Q(content__icontains=keywords)
        )
        additional_params.append(
            '&keywords=' + urllib.parse.quote_plus(keywords)
        )

    return (articles, ''.join(additional_params))


def apply_pagination(request, articles, per_page):
    return Paginator(articles, per_page).get_page(request.GET.get('page'))


def load_articles():
    articles = Article.objects.order_by('-created_at')

    return articles.filter(published=True).filter(published_at__lte=timezone.now())


def load_authors():
    return Author.objects.order_by('name')

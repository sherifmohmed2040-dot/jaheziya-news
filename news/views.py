from django.shortcuts import render
from .models import Article


def home(request):
    featured_article = Article.objects.filter(featured=True, image__isnull=False).exclude(image="").first()
    latest_articles = Article.objects.all()[:6]

    return render(request, "news/home.html", {
        "featured_article": featured_article,
        "latest_articles": latest_articles,
    })
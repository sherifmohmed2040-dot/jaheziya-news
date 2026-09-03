from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "featured", "published_at")
    list_filter = ("category", "featured")
    search_fields = ("title", "summary")
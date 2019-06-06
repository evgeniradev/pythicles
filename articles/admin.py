from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Article


class ArticleAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    exclude = ['created_at', 'updated_at']

admin.site.register(Article, ArticleAdmin)

from django.db import models
from django.utils import timezone
from authors.models import Author


class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/articles/%Y/%m/%d/')
    content = models.TextField()
    slug = models.SlugField(max_length=70, unique=True)
    published = models.BooleanField(default=True)
    published_at = models.DateTimeField(default=timezone.now, blank=True)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    updated_at = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.title

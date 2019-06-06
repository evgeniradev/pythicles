from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=40, unique=True)

    def __str__(self):
        return self.name

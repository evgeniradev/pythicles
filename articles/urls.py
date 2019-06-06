from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('article/<slug:article_slug>', views.article, name='article')
]

from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from django.utils import timezone
from authors.models import Author
from .models import Article
from . import views

import tempfile


class ArticleTestCase(TestCase):
    def setUp(self):
        self.client = Client()

        image = tempfile.NamedTemporaryFile(suffix='.jpg').name

        user1 = User.objects.create(username='user1_username')
        user2 = User.objects.create(username='user2_username')

        self.author1 = Author.objects.create(
            name='B Author1 name', user=user1, slug='author1-slug'
        )
        self.author2 = Author.objects.create(
            name='A Author2 name', user=user2, slug='author2-slug'
        )

        self.article1 = Article.objects.create(
            title='Article1 title',
            content='Test content',
            slug='article1-slug',
            image=image,
            author=self.author1
        )
        self.article2 = Article.objects.create(
            title='Article2 title',
            content='Test content',
            slug='article2-slug',
            image=image,
            author=self.author2
        )

    def test_index_returns_articles_in_created_at_desc_order(self):
        response = self.client.get('/')

        self.assertEqual(
            response.context['articles'].object_list,
            [self.article2, self.article1]
        )

    def test_index_does_not_return_articles_with_future_publish_time(self):
        self.article1.published_at = timezone.now() + timezone.timedelta(hours=1)
        self.article1.save()

        response = self.client.get('/')

        self.assertEqual(
            response.context['articles'].object_list,
            [self.article2]
        )

    def test_index_does_not_return_articles_that_are_manually_unpublished(self):
        self.article1.published = False
        self.article1.save()

        response = self.client.get('/')

        self.assertEqual(
            response.context['articles'].object_list,
            [self.article2]
        )

    def test_index_paginates_articles(self):
        response = self.client.get('/')

        self.assertEqual(response.context['articles'].paginator.num_pages, 1)

    def test_index_sets_displayed_pages_margin_to_3(self):
        response = self.client.get('/')

        self.assertEqual(response.context['displayed_pages_margin'], 3)

    def test_index_filters_by_case_insensitive_keywords(self):
        response = self.client.get(f'/?keywords={self.article1.title.lower()}')

        self.assertEqual(
            response.context['articles'].object_list,
            [self.article1]
        )

    def test_index_sets_additional_params_when_filters_by_keywords(self):
        response = self.client.get(f'/?keywords={self.article1.title.lower()}')

        self.assertEqual(
            response.context['additional_params'],
            '&keywords=article1+title'
        )

    def test_index_filters_by_author_slug(self):
        response = self.client.get(f'/?author={self.author2.slug}')

        self.assertEqual(
            response.context['articles'].object_list,
            [self.article2]
        )

    def test_index_sets_additional_params_when_filters_by_author_slug(self):
        response = self.client.get(f'/?author={self.author2.slug}')

        self.assertEqual(
            response.context['additional_params'],
            f'&author={self.author2.slug}'
        )

    def test_index_returns_authors_in_alphabetical_order(self):
        response = self.client.get('/')

        self.assertEqual(
            list(response.context['authors']),
            [self.author2, self.author1]
        )

    def test_article_returns_article(self):
        response = self.client.get(f'/article/{self.article1.slug}')

        self.assertEqual(response.context['article'], self.article1)

    def test_article_returns_authors_in_alphabetical_order(self):
        response = self.client.get(f'/article/{self.article1.slug}')

        self.assertEqual(
            list(response.context['authors']),
            [self.author2, self.author1]
        )

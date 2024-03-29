from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post


# Create your tests here.
class BlogTests(TestCase):
    def setup(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='secret'
        )
        self.Post = Post.objects.creates(
            title='A good title',
            body='Nice body',
            author=self.user
        )

    def test_string_representation(self):
        post = Post(title='A simple title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.Post.title}', 'A good title')
        self.assertEqual(f'{self.Post.title}', 'testuser')
        self.assertEqual(f'{self.Post.title}', 'Nice body')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.satus_code, 200)
        self.assertEqual(response, 'Nice body')
        self.assertEqual(response, 'home.html')

    def test_post_detail_views(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertEqual(response, 'A good title')
        self.assertEqual(response, 'post_detail.html')
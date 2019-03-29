from django.test import TestCase, Client
from ..views import PostCreateView
from django.contrib.auth.models import User
from ..models import Post
import random
from django.urls import reverse

class PostViewTest(TestCase):
    def setUp(self):
        '''This is ran before each and every test!
        We want to ensure that all these posts are being rendered'''
        self.user = User.objects.create_user(username='test_user', password='password123')
        self.post = Post.objects.create(title='test post', content='test post', author=self.user)
        self.post1 = Post.objects.create(title='test post', content='test post1', author=self.user)
        self.post2 = Post.objects.create(title='test post', content='test post2', author=self.user)
        self.post3 = Post.objects.create(title='test post', content='test post3', author=self.user)
        self.post4 = Post.objects.create(title='test post', content='test post4', author=self.user)
        self.post5 = Post.objects.create(title='test post', content='test post5', author=self.user)

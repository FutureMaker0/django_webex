from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Post, Comment, HashTag, Category

# Create your tests here.

# class TestView(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.user_trump = User.objects.create_user(username='trump', password='somepassword')
#         self.user_obama = User.objects.create_user(username='obama', password='somepassword')

#         self.category_programming = Category.objects.create(name='programming', slug='programming')
#         self.category_music = Category.objects.create(name='music', slug='music')



from turtle import title
from venv import create

from django.contrib.auth.models import User
from django.db import models
# Create your models here.
from django.utils import timezone


class Post(models.Model):
    STATUS__CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS__CHOICES, default='draft')

    class Meta:
        ordering = ('-publish', )

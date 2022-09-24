
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
# Create your models here.
from django.utils import timezone


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


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
    objects = models.Manager()
    published_objects = PublishedManager()

    class Meta:
        ordering = ('-publish', )

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year, self.publish.month,
                                                 self.publish.day, self.slug])

from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    thumb = models.ImageField(default='default.png', blank=True, upload_to='images/')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def snippet(self):
        return self.content[:50] + '...'

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug, 'id':self.id})

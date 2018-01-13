#from blog.models import Post
from django.db import models
from taggit.managers import TaggableManager

class Post(models.Model):
    title = models.CharField(max_length = 140)
    body = models.TextField()
    date = models.DateTimeField()
    tags = models.CharField(max_length =50)

    def __str__(self):
        return self.title

def get_rlated(tag):
    post = Post.objects.filter(tags__icontains=tag).order_by("-date")[:25]

    return post

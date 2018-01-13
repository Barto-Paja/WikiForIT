from django.db import models
from taggit.managers import TaggableManager
# Create your models here.



class Post(models.Model):
    title = models.CharField(max_length = 140)
    body = models.TextField()
    date = models.DateTimeField()
    tags = models.CharField(max_length =50)
    #tags = TaggableManager()

    def __str__(self):
        return self.title

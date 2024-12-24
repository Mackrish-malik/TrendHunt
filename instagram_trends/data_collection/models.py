from django.db import models

class Hashtag(models.Model):
    name = models.CharField(max_length=255)
    usage_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    caption = models.TextField()
    media_type = models.CharField(max_length=50)
    media_url = models.URLField()
    hashtags = models.ManyToManyField(Hashtag)
    created_at = models.DateTimeField(auto_now_add=True)

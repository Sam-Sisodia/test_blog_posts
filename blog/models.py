from django.db import models
    
# Create your models here.

class InstaPassword(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

class PostHashTag(models.Model):
    hashtag = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.hashtag

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description  = models.CharField(max_length=200)
    date_time = models.DateTimeField(auto_now=True)
    summary = models.TextField()
    
    hashtags = models.ManyToManyField(PostHashTag, related_name='blog_posts', blank=True)

    def __str__(self):
        return self.title


class Blog_Commnet(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.PROTECT)
    comment = models.CharField(max_length=200)
    date_time = models.DateTimeField(auto_now=True)
    email = models.EmailField(blank=False , null=True)

class Share_Blog(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.PROTECT)
    token = models.CharField(max_length=200)
    date_time = models.DateTimeField(auto_now=True)
    email = models.EmailField(blank=False , null=True)


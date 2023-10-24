from django.db import models
from AuthApp.models import AuthorUser


# Create your models here.

class BlogModel(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    publish_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    author = models.ForeignKey(AuthorUser, on_delete=models.CASCADE, null=True, blank=True)
    tags = models.ManyToManyField('Tag', related_name='blogs', blank=True, null=True)
    is_published = models.BooleanField(default=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"{self.title}--{self.id}"


class BlogImage(models.Model):
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    caption = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Image for {self.blog.title}"


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


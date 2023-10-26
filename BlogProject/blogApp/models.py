from django.db import models
from AuthApp.models import AuthorUser


class BlogImage(models.Model):
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    caption = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.id}"


class Tag(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class BlogModel(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    publish_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    is_published = models.BooleanField(default=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    author = models.ForeignKey(AuthorUser, on_delete=models.CASCADE, null=True, blank=True, related_name='blog_posts')
    blogImage = models.ForeignKey(BlogImage, on_delete=models.CASCADE, related_name='images', null=True, blank=True)
    tag = models.ManyToManyField(Tag, related_name='tag', blank=True)

    def __str__(self):
        return f"{self.title}"

from django.db import models
from AuthApp.models import AuthorUser

# Create your models here.

class BlogModel(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(AuthorUser, on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    tags = models.ManyToManyField('Tag', related_name='blogs', blank=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}--{self.id}"

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



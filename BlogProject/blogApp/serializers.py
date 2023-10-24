from rest_framework import serializers
from .models import BlogModel, BlogImage, Tag
from AuthApp.models import AuthorUser


class PostBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = "__all__"

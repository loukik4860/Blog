from rest_framework import serializers
from .models import BlogModel, BlogImage, Tag
from AuthApp.models import AuthorUser



class PostBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = "__all__"

class BlogImageSerializer(serializers.ModelSerializer):
    blog = PostBlogSerializer(read_only=True)
    class Meta:
        model = BlogImage
        fields = ['id','image','caption','blog']


class TagSerializer(serializers.ModelSerializer):
    blog = PostBlogSerializer(read_only=True)
    image = BlogImageSerializer(read_only=True)
    class Meta:
        model = Tag
        fields = ['id','name','blog','image']
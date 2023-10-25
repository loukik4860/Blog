from rest_framework import serializers
from .models import BlogModel, BlogImage, Tag
from AuthApp.models import AuthorUser


class AuthorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorUser
        fields = ['id', 'Author_email', 'Author_firstName', 'Author_lastName', 'created_at', 'updated_at']


class BlogImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogImage
        fields = ['id', 'image', 'caption']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class BlogModelSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    blogImage = BlogImageSerializer()
    tag = TagSerializer(many=True)

    class Meta:
        model = BlogModel
        fields = ['id', 'title', 'content', 'publish_date', 'is_published', 'created_at', 'updated_at',
                  'blogImage', 'tag', 'author']


class PostBlogSerializer(serializers.ModelSerializer):
    post = AuthorProfileSerializer(many=True)

    class Meta:
        model = AuthorUser
        fields = ['Author_email', 'Author_firstName', 'Author_lastName', 'is_author', 'is_active', 'is_admin',
                  'created_at', 'updated_at', 'post', 'author']


class AuthorAllDetailsSerializer(serializers.ModelSerializer):
    blog_posts = BlogModelSerializer(many=True)

    class Meta:
        model = AuthorUser
        fields = ['Author_email', 'Author_firstName', 'Author_lastName', 'is_author', 'is_active', 'is_admin',
                  'created_at', 'updated_at', 'blog_posts']

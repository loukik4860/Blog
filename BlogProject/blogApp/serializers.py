from rest_framework import serializers
from .models import BlogModel, BlogImage, Tag
from AuthApp.models import AuthorUser


class BlogImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogImage
        fields = ['id', 'image', 'caption']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class BlogModelSerializer(serializers.ModelSerializer):
    blogImage = BlogImageSerializer()
    tag = TagSerializer(many=True)

    class Meta:
        model = BlogModel
        fields = ['id', 'title', 'content', 'publish_date', 'is_published', 'created_at', 'updated_at', 'author',
                  'blogImage', 'tag']


# class AuthorProfileSer(serializers.ModelSerializer):
#     author_post = BlogModelSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = AuthorUser
#         fields = ['id', 'Author_email', 'Author_firstName', 'Author_lastName', 'created_at', 'updated_at',
#                   'author_post']


class PostBlogSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = BlogModel
        fields = ['id', 'title', 'content', 'publish_date', 'is_published', 'created_at', 'updated_at',
                  'author']

from rest_framework import views
from .serializers import PostBlogSerializer, BlogImageSerializer, TagSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import BlogModel, BlogImage, Tag
from AuthApp.models import AuthorUser
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthor
from rest_framework_simplejwt.authentication import JWTAuthentication


class PostBlogView(ListCreateAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = PostBlogSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class PostBlogDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = PostBlogSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthor]


class PostBlogImageView(ListCreateAPIView):
    queryset = BlogImage.objects.all()
    serializer_class = BlogImageSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class PostBlogImageDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = BlogImage.objects.all()
    serializer_class = BlogImageSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthor]


class PostTagView(ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class PostTagDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthor]

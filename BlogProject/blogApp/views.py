from rest_framework import views
from .serializers import BlogImageSerializer, TagSerializer, BlogModelSerializer, AuthorProfileSerializer,AuthorAllDetailsSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView,RetrieveAPIView
from .models import BlogModel, BlogImage, Tag
from AuthApp.models import AuthorUser
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthor
from rest_framework_simplejwt.authentication import JWTAuthentication


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


class PostBlogView(ListCreateAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogModelSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class PostBlogDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogModelSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthor]

class BlogView(ListAPIView):
    pass


class AuthorPostView(ListAPIView):
    queryset = AuthorUser.objects.all()
    serializer_class = AuthorProfileSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthor]


class AuthorAllDetails(ListAPIView):
    queryset = AuthorUser.objects.all()
    serializer_class = AuthorAllDetailsSerializer

class AuthorDetails(RetrieveAPIView):
    queryset = AuthorUser.objects.all()
    serializer_class = AuthorAllDetailsSerializer
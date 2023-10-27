from rest_framework import views, filters
from .serializers import BlogImageSerializer, TagSerializer, BlogModelSerializer, AuthorProfileSerializer, \
    AuthorAllDetailsSerializer, NestedTagSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView
from .models import BlogModel, BlogImage, Tag
from AuthApp.models import AuthorUser
from .filters import AuthorUserFilter
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsAuthor
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from django_filters.rest_framework import DjangoFilterBackend


class PostBlogImageView(ListCreateAPIView):
    queryset = BlogImage.objects.all()
    serializer_class = BlogImageSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class PostBlogImageDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = BlogImage.objects.all()
    serializer_class = BlogImageSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]


class PostTagView(ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    filterset_fields = ['name']

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class PostTagDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    throttle_classes = [AnonRateThrottle]


class PostBlogView(ListCreateAPIView):  ######
    queryset = BlogModel.objects.all()
    serializer_class = BlogModelSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    # filterset_fields = ['title', "content",'blog_posts__tag__name']
    filterset_fields = {
        'title': ['icontains'],
        'content': ['icontains'],
    }
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class PostBlogDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogModelSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]


class BlogView(ListAPIView):
    pass


class AuthorPostView(ListAPIView):
    queryset = AuthorUser.objects.all()
    serializer_class = AuthorProfileSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    filterset_fields = ['Author_firstName', "Author_lastName"]


class AllAuthorDetailsWithBlogPost_blogImage_tags(ListAPIView):
    queryset = AuthorUser.objects.all()
    serializer_class = AuthorAllDetailsSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter,
                       filters.SearchFilter]  # filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = AuthorUserFilter
    filterset_fields = {
        'Author_firstName': ['icontains'],
        'Author_lastName': ['icontains'],
        'blog_posts__tag__name': ['icontains'],
    }


class AuthorDetailsWithBlogPost_blogImage_tags(RetrieveAPIView):
    queryset = AuthorUser.objects.all()
    serializer_class = AuthorAllDetailsSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]


class TagDetailsWithPost(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = NestedTagSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
from rest_framework import views
from .serializers import PostBlogSerializer
from rest_framework.generics import ListCreateAPIView
from .models import BlogModel,BlogImage,Tag
from AuthApp.models import AuthorUser

class PostBlogView(ListCreateAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = PostBlogSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request,*args,**kwargs)

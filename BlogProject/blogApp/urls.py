from django.urls import path
from .views import PostBlogView

urlpatterns = [
    path('postblog/',PostBlogView.as_view(),name="postblog")
]
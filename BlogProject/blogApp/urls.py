from django.urls import path
from .views import PostBlogView,PostBlogDetailsView,PostBlogImageView,PostBlogImageDetailsView,PostTagView,PostTagDetailsView

urlpatterns = [
    path('postblog/',PostBlogView.as_view(),name="postblog"),
    path('postblog/<int:pk>/',PostBlogDetailsView.as_view(),name="postblogDetails"),
    path('postImage/',PostBlogImageView.as_view(),name="postImage"),
    path('postImage/<int:pk>/',PostBlogImageDetailsView.as_view(),name="postdetails"),
    path('tag/',PostTagView.as_view(),name="postTag"),
    path('tag/<int:pk>/',PostTagDetailsView.as_view(),name="postTagDetails"),
]
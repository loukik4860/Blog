from django.urls import path
from .views import PostBlogImageView,PostBlogImageDetailsView,PostTagView,PostTagDetailsView,PostBlogView,PostBlogDetailsView,AuthorPostView

urlpatterns = [
    path('postImage/', PostBlogImageView.as_view(), name="postImage"),
    path('postImage/<int:pk>/', PostBlogImageDetailsView.as_view(), name="postdetails"),
    path('tagpost/', PostTagView.as_view(), name="postTag"),
    path('tagpost/<int:pk>/', PostTagDetailsView.as_view(), name="postTagDetails"),
    path('postblog/',PostBlogView.as_view(),name="postblog"),
    path('postblog/<int:pk>/',PostBlogDetailsView.as_view(),name="postblogDetails"),
    path('authorlist/',AuthorPostView.as_view(),name="authorPost")
]
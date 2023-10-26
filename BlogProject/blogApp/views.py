from rest_framework import views
from .serializers import BlogImageSerializer, TagSerializer, BlogModelSerializer, AuthorProfileSerializer, \
    AuthorAllDetailsSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView
from .models import BlogModel, BlogImage, Tag
from AuthApp.models import AuthorUser
from rest_framework.permissions import IsAuthenticated,AllowAny
from .permissions import IsAuthor
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle

class PostBlogImageView(ListCreateAPIView):
    """
       API endpoint for managing blog post images.

       This view allows users to create and list blog post images. It supports
       the following HTTP methods:
       - GET: Retrieve a list of blog post images.
       - POST: Create a new blog post image.

       Permissions:
       - Users must be authenticated using JWTAuthentication to access this view.
       - Users must have 'IsAuthor' permission to create a new blog post image.

       Attributes:
       - queryset (QuerySet): All available blog post images in the database.
       - serializer_class (Serializer): Serializer for serializing blog post image data.
       - authentication_classes (list): JWTAuthentication is used for authentication.
       - permission_classes (list): 'IsAuthor' permission is required for POST requests.

       Example:
       - GET request to 'postImage/' retrieves a list of blog post images.
       - POST request to 'postImage/' creates a new blog post image.
       - GET, PUT, DELETE requests to 'postImage/<int:pk>/' allow you to retrieve, update, or delete a specific blog post image.
       """
    queryset = BlogImage.objects.all()
    serializer_class = BlogImageSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthor]

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class PostBlogImageDetailsView(RetrieveUpdateDestroyAPIView):
    """
       API endpoint for managing a specific blog post image.

       This view allows users to retrieve, update, or delete a specific blog post image based on its ID.

       Supported HTTP methods:
       - GET: Retrieve details of a specific blog post image.
       - PUT: Update the data of a specific blog post image.
       - DELETE: Delete a specific blog post image.

       Permissions:
       - Users must be authenticated using JWTAuthentication to access this view.
       - Users must have 'IsAuthor' permission to perform updates or deletions.

       Attributes:
       - queryset (QuerySet): All available blog post images in the database.
       - serializer_class (Serializer): Serializer for serializing blog post image data.
       - authentication_classes (list): JWTAuthentication is used for authentication.
       - permission_classes (list): 'IsAuthor' permission is required for PUT and DELETE requests.

       URL Pattern:
       - To retrieve details of a specific blog post image, use the URL pattern 'postImage/<int:pk>/' (GET).
       - To update a specific blog post image, use the URL pattern 'postImage/<int:pk>/' (PUT).
       - To delete a specific blog post image, use the URL pattern 'postImage/<int:pk>/' (DELETE).

       Example:
       - GET request to 'postImage/<int:pk>/' retrieves details of a specific blog post image.
       - PUT request to 'postImage/<int:pk>/' updates the data of a specific blog post image.
       - DELETE request to 'postImage/<int:pk>/' deletes a specific blog post image.

       URL Parameters:
       - int:pk (int): The unique identifier of the blog post image to retrieve, update, or delete.
       """
    queryset = BlogImage.objects.all()
    serializer_class = BlogImageSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthor]


class PostTagView(ListCreateAPIView):
    class PostTagView(ListCreateAPIView):
        """
        API endpoint for managing blog post tags.

        This view allows users to retrieve a list of all available blog post tags or create new tags.

        Supported HTTP methods:
        - GET: Retrieve a list of all available blog post tags.
        - POST: Create a new tag.

        Permissions:
        - Users must be authenticated using JWTAuthentication to access this view.
        - All authenticated users can retrieve the list of tags.
        - Creating new tags is allowed for all authenticated users.

        Attributes:
        - queryset (QuerySet): All available blog post tags in the database.
        - serializer_class (Serializer): Serializer for serializing tag data.
        - authentication_classes (list): JWTAuthentication is used for authentication.
        - permission_classes (list): All authenticated users have permission to retrieve tags.
          Creating new tags is allowed for all authenticated users.

        URL Pattern:
        - To retrieve a list of all available blog post tags, use the URL pattern 'tags/' (GET).
        - To create a new tag, use the URL pattern 'tags/' (POST).

        Example:
        - GET request to 'tags/' retrieves a list of all available blog post tags.
        - POST request to 'tags/' creates a new tag.

        Request Data (POST):
        - When creating a new tag, send a JSON object with the tag data:
            {
                "name": "Tag Name"
            }

        Response Data (GET):
        - The response will include a list of blog post tags.

        URL Parameters:
        - None

        JSON Object Fields:
        - name (str): The name of the tag to be created.

        Response Status Codes:
        - 201 Created: When a new tag is successfully created.
        - 200 OK: When retrieving the list of tags is successful.
        """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class PostTagDetailsView(RetrieveUpdateDestroyAPIView):
    """
    API endpoint for managing blog post tags.

    This view allows users to retrieve a list of all available blog post tags or create new tags.

    Supported HTTP methods:
    - GET: Retrieve a list of all available blog post tags.
    - POST: Create a new tag.

    Permissions:
    - Users must be authenticated using JWTAuthentication to access this view.
    - All authenticated users can retrieve the list of tags.
    - Creating new tags is allowed for all authenticated users.

    Throttling:
    - Rate throttling is applied to limit the number of requests from anonymous users.
    - Authenticated users are not affected by rate throttling.

    Attributes:
    - queryset (QuerySet): All available blog post tags in the database.
    - serializer_class (Serializer): Serializer for serializing tag data.
    - authentication_classes (list): JWTAuthentication is used for authentication.
    - permission_classes (list): All authenticated users have permission to retrieve tags.
      Creating new tags is allowed for all authenticated users.
    - throttle_classes (list): AnonRateThrottle is used to limit anonymous user access.

    URL Pattern:
    - To retrieve a list of all available blog post tags, use the URL pattern 'tags/' (GET).
    - To create a new tag, use the URL pattern 'tags/' (POST).

    Example:
    - GET request to 'tags/' retrieves a list of all available blog post tags.
    - POST request to 'tags/' creates a new tag.

    Request Data (POST):
    - When creating a new tag, send a JSON object with the tag data:
        {
            "name": "Tag Name"
        }

    Response Data (GET):
    - The response will include a list of blog post tags.

    URL Parameters:
    - None

    JSON Object Fields:
    - name (str): The name of the tag to be created.

    Response Status Codes:
    - 201 Created: When a new tag is successfully created.
    - 200 OK: When retrieving the list of tags is successful.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthor]
    throttle_classes = [AnonRateThrottle]

class PostBlogView(ListCreateAPIView):
    """
        API endpoint for managing blog posts.

        This view allows users to retrieve a list of all blog posts or create new blog posts.

        Supported HTTP methods:
        - GET: Retrieve a list of all available blog posts.
        - POST: Create a new blog post.

        Permissions:
        - Users must be authenticated using JWTAuthentication to access this view.
        - All authenticated users can retrieve the list of blog posts.
        - Creating new blog posts is allowed for all authenticated users.

        Attributes:
        - queryset (QuerySet): All available blog posts in the database.
        - serializer_class (Serializer): Serializer for serializing blog post data.
        - authentication_classes (list): JWTAuthentication is used for authentication.
        - permission_classes (list): All authenticated users have permission to retrieve blog posts.
          Creating new blog posts is allowed for all authenticated users.

        URL Pattern:
        - To retrieve a list of all available blog posts, use the URL pattern 'posts/' (GET).
        - To create a new blog post, use the URL pattern 'posts/' (POST).

        Example:
        - GET request to 'posts/' retrieves a list of all available blog posts.
        - POST request to 'posts/' creates a new blog post.

        Request Data (POST):
        - When creating a new blog post, send a JSON object with the blog post data.
        - Ensure the 'author' field is specified to associate the post with a specific author.

        Response Data (GET):
        - The response will include a list of blog posts.

        URL Parameters:
        - None

        JSON Object Fields (POST):
        - title (str): The title of the blog post.
        - content (str): The content of the blog post.
        - is_published (bool): Indicates whether the post is published.
        - author (int): The author's user ID (associated with the post).
        - blogImage (dict): Dictionary containing 'image' (str) and 'caption' (str).
        - tag (list of ints): List of tag IDs associated with the post.

        Response Status Codes:
        - 201 Created: When a new blog post is successfully created.
        - 200 OK: When retrieving the list of blog posts is successful.
        """
    queryset = BlogModel.objects.all()
    serializer_class = BlogModelSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class PostBlogDetailsView(RetrieveUpdateDestroyAPIView):
    """
        API endpoint for managing a specific blog post.

        This view allows users to retrieve, update, or delete a specific blog post by its ID.

        Supported HTTP methods:
        - GET: Retrieve the details of a specific blog post.
        - PUT: Update a specific blog post.
        - DELETE: Delete a specific blog post.

        Permissions:
        - Users must be authenticated using JWTAuthentication to access this view.
        - Users can retrieve, update, and delete their own blog posts.
        - Users with permission to delete a blog post can also update and retrieve it.

        Attributes:
        - queryset (QuerySet): All available blog posts in the database.
        - serializer_class (Serializer): Serializer for serializing blog post data.
        - authentication_classes (list): JWTAuthentication is used for authentication.
        - permission_classes (list): Users can retrieve, update, and delete their own blog posts.

        URL Pattern:
        - To retrieve, update, or delete a specific blog post, use the URL pattern 'posts/<int:pk>/'.

        Example:
        - GET request to 'posts/1/' retrieves the details of blog post with ID 1.
        - PUT request to 'posts/1/' updates the blog post with ID 1.
        - DELETE request to 'posts/1/' deletes the blog post with ID 1.

        Request Data (PUT):
        - Send a JSON object with the updated blog post data.

        Response Data (GET):
        - The response will include the details of the specific blog post.

        URL Parameters:
        - pk (int): The primary key of the specific blog post.

        JSON Object Fields (PUT):
        - title (str): The updated title of the blog post.
        - content (str): The updated content of the blog post.
        - is_published (bool): Indicates whether the post is published.
        - blogImage (dict): Dictionary containing 'image' (str) and 'caption' (str).
        - tag (list of ints): List of updated tag IDs associated with the post.

        Response Status Codes:
        - 200 OK: When retrieving the blog post details is successful.
        - 204 No Content: When the blog post is successfully updated or deleted.
        """
    queryset = BlogModel.objects.all()
    serializer_class = BlogModelSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthor]


class BlogView(ListAPIView):
    pass


class AuthorPostView(ListAPIView):
    """
        API endpoint for listing author profiles.

        This view allows users to retrieve a list of author profiles.

        Supported HTTP methods:
        - GET: Retrieve a list of author profiles.

        Permissions:
        - Users must be authenticated using JWTAuthentication to access this view.
        - Users can retrieve a list of author profiles.

        Attributes:
        - queryset (QuerySet): All available author profiles in the database.
        - serializer_class (Serializer): Serializer for serializing author profile data.
        - authentication_classes (list): JWTAuthentication is used for authentication.
        - permission_classes (list): Users can retrieve a list of author profiles.

        URL Pattern:
        - The URL pattern for this view is '/authorProfiles/'.

        Example:
        - GET request to '/authorProfiles/' retrieves a list of all author profiles.

        Response Data (GET):
        - The response will include a list of author profiles, each with their details.

        Response Status Codes:
        - 200 OK: When retrieving the list of author profiles is successful.
        """
    queryset = AuthorUser.objects.all()
    serializer_class = AuthorProfileSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthor]


class AuthorAllDetails(ListAPIView):
    """
       API endpoint for retrieving detailed author information.

       This view allows users to retrieve detailed information about authors, including their blog posts, images, and tags.

       Supported HTTP methods:
       - GET: Retrieve detailed information about authors.

       Permissions:
       - This view is accessible to all users without authentication (AllowAny).

       Attributes:
       - queryset (QuerySet): All available author profiles in the database.
       - serializer_class (Serializer): Serializer for serializing detailed author information.
       - authentication_classes (list): JWTAuthentication is used for authentication, but it is not required.
       - permission_classes (list): All users can retrieve detailed author information.

       URL Pattern:
       - The URL pattern for this view is '/authorDetails/'.

       Example:
       - GET request to '/authorDetails/' retrieves detailed information about authors, including their blog posts, images, and tags.

       Response Data (GET):
       - The response will include detailed information about authors, including their blog posts, images, and tags.

       Response Status Codes:
       - 200 OK: When retrieving detailed author information is successful.
       """
    queryset = AuthorUser.objects.all()
    serializer_class = AuthorAllDetailsSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]


class AuthorDetails(RetrieveAPIView):
    """
       API endpoint for retrieving detailed information about a specific author.

       This view allows users to retrieve detailed information about a specific author, including their blog posts, images, and tags.

       Supported HTTP methods:
       - GET: Retrieve detailed information about a specific author.

       Permissions:
       - This view is accessible to all users without authentication (AllowAny).

       Throttling:
       - Throttling classes, AnonRateThrottle and UserRateThrottle, are applied to limit the rate of requests for both anonymous users and authenticated users.

       Attributes:
       - queryset (QuerySet): All available author profiles in the database.
       - serializer_class (Serializer): Serializer for serializing detailed author information.
       - authentication_classes (list): JWTAuthentication is used for authentication, but it is not required.
       - permission_classes (list): All users can retrieve detailed author information.
       - throttle_classes (list): AnonRateThrottle and UserRateThrottle are applied for request throttling.

       URL Pattern:
       - The URL pattern for this view is '/authorDetails/<int:pk>/', where '<int:pk>' is the primary key of the author.

       Example:
       - GET request to '/authorDetails/1/' retrieves detailed information about the author with ID 1, including their blog posts, images, and tags.

       Response Data (GET):
       - The response will include detailed information about the specified author, including their blog posts, images, and tags.

       Response Status Codes:
       - 200 OK: When retrieving detailed author information is successful.
       - 429 Too Many Requests: When the request rate limit is exceeded (throttling).
       """
    queryset = AuthorUser.objects.all()
    serializer_class = AuthorAllDetailsSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    throttle_classes = [AnonRateThrottle,UserRateThrottle]
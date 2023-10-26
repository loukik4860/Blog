from django.contrib import admin
from .models import BlogModel, BlogImage, Tag

# Register your models with the admin site here.

@admin.register(BlogModel)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_date', 'author', 'is_published')
    list_filter = ('is_published', 'publish_date')
    search_fields = ('title', 'author__username')
    list_per_page = 25  # Number of items to show per page

@admin.register(BlogImage)
class BlogImageAdmin(admin.ModelAdmin):
    list_display = ('id','image','caption',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id','name',)

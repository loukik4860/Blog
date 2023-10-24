from django.contrib import admin
from .models import BlogModel, Tag, BlogImage


@admin.register(BlogModel)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_date', 'is_published')
    list_filter = ('is_published', 'publish_date')
    search_fields = ('title', 'content')
    date_hierarchy = 'publish_date'
    filter_horizontal = ('tags',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


class BlogImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'blog', 'caption')
    list_filter = ('blog',)
    search_fields = ('caption',)
    list_per_page = 20  # Customize the number of items displayed per page
    list_display_links = ('id', 'caption')  # Add links to these fields in the list view


admin.site.register(BlogImage, BlogImageAdmin)

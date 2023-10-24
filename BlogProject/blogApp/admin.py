from django.contrib import admin
from .models import BlogModel, Tag


@admin.register(BlogModel)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date', 'is_published')
    list_filter = ('is_published', 'pub_date')
    search_fields = ('title', 'content')
    date_hierarchy = 'pub_date'
    filter_horizontal = ('tags',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

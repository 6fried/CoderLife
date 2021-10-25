from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('en_title', 'fr_title', 'slug', 'author', 'pub_date', 'status')
    list_filter = ('status', 'created_at', 'pub_date', 'author')
    search_fields = ('en_title', 'fr_title', 'en_content', 'fr_content')
    prepopulated_fields = {'slug': ('en_title',)}
    ordering = ('status', 'pub_date')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

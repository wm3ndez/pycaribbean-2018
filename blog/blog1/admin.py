from django.contrib import admin

from blog.blog1.models import Post, PostComment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'approved', 'category')
    list_filter = ('approved',)


@admin.register(PostComment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post')

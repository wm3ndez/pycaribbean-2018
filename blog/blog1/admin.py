from django.contrib import admin

from blog.blog1.models import Post, PostComment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'approved')


@admin.register(PostComment)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post')

from django.contrib import admin

from .models import Comment, Post, User  # Comment を追加

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)
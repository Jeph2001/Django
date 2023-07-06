from django.contrib import admin
from .models import Board, Topic, Post
# Register your models here.


class BoardAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class TopicAdmin(admin.ModelAdmin):
    list_display = ('subject', 'last_updated', 'board', 'starter')


class PostAdmin(admin.ModelAdmin):
    list_display = ('message', 'topic', 'created_at', 'updated_at', 'created_by', 'updated_by')



admin.site.register(Board, BoardAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Post, PostAdmin)

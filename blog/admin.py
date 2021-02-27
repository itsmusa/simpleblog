from django.contrib import admin

from . models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date', 'updated')
    search_fields = ('title', 'body')

from django.contrib import admin
from .models import Author, BlogCategory, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


# Register your models here.
admin.site.register(Author, AuthorAdmin)
admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(Post, PostAdmin)

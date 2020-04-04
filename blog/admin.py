from django.contrib import admin
from .models import Author, Category, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}


# Register your models here.
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)

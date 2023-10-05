from django.contrib import admin
from .models import Category, Post, User

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'author']
    list_display = ['title', 'author', 'overview', 'timestamp']
    prepopulated_fields = {'slug' : ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title', 'slug']
    list_display = ['title']
    prepopulated_fields = {'slug' : ('title',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(User)
from django.contrib import admin
from .models import Category, Post, User, Comment

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'author']
    list_display = ['title', 'author', 'overview', 'timestamp']
    prepopulated_fields = {'slug' : ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title', 'slug']
    list_display = ['title']
    prepopulated_fields = {'slug' : ('title',)}

class UserAdmin(admin.ModelAdmin):
    search_fields = ['username']
    list_display = ['username', 'email', 'is_active', 'is_staff']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Comment)
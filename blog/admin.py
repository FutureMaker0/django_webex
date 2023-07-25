from django.contrib import admin
from .models import Post, Comment, HashTag, Category

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(HashTag)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Category, CategoryAdmin)

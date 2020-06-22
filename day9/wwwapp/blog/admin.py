from django.contrib import admin

# Register your models here.
from blog.models import Post

# admin.site.register(Post)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}
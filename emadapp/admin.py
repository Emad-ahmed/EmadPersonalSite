from django.contrib import admin
from emadapp.models import BlogPost
# Register your models here.


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['id']

from django.contrib import admin
from .models import BlogPost
from markdownx.admin import MarkdownxModelAdmin

# @admin.register(BlogPost, MarkdownxModelAdmin)
# class BlogPostAdmin(admin.ModelAdmin):
#     pass

admin.site.register(BlogPost, MarkdownxModelAdmin)

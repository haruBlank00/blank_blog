from django.contrib import admin
from .models import TagModel

@admin.register(TagModel)
class TagModel(admin.ModelAdmin):
    pass

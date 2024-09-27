from django.db import models

# Create your models here.
class CategoryModel(models.Model):
    # Name of the category
    # EG: Lifestyle, Programming
    name = models.CharField(max_length=255)

    # Description of the category
    # EG: Life style articles
    description = models.TextField()

    # Is the category published
    is_published = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
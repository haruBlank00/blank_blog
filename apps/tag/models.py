from django.db import models

class TagModel(models.Model):
    # Name of the tag
    # EG: python, django, etc
    name = models.CharField(max_length=255)

    # Description of the tag
    # EG: Python programming language
    #     Django web framework
    description = models.TextField()

    # Is the tag published
    # EG: True, False
    is_published = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
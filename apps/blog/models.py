from django.db import models

# Create your models here.
class BlogPost(models.Model):
    # Blog title
    # EG: My First Blog
    title = models.CharField(max_length=255)

    # MD Format content
    # EG: # My First Blog
    content = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Is it published?
    is_published = models.BooleanField(default=False)

    # Category of the post
    # EG: Programming, Lifestyle
    category = models.ForeignKey('category.CategoryModel', on_delete=models.CASCADE)

    # Tags of the post
    # EG: Python, Django
    tags = models.ManyToManyField('tag.TagModel', blank=True)

    def __str__(self):
        return self.title

    

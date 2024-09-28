from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BlogPost
""" class BlogView:

    def index(request):
        return render(request, 'blog/index.html')
   """  

"""
Generic List view to list the blog posts
url: /
"""
""" class BlogView(ListView):
    model = BlogPost
    # context_object_name = 'blogPosts'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['blogPosts'] = BlogPost.objects.all()
        return context """
    

class BlogListView(ListView):
    queryset = BlogPost.objects.order_by("-created_at")
    context_object_name = "blog_posts"
    template_name = "blog/blogpost_list.html"

class BlogDetailView(DetailView):
    model = BlogPost
    context_object_name = "blog_post"
    template_name = "blog/blogpost_details.html"
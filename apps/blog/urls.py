from django.urls import path
from .views import BlogListView, BlogDetailView

""" urlpatterns = [
    path('', BlogView.index, name='index'),
] """
urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name='blogpost_detail'),
]
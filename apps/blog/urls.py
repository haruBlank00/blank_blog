from django.urls import path
from .views import BlogView

urlpatterns = [
    path('', BlogView.index, name='index'),
]
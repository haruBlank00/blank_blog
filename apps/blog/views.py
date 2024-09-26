from django.shortcuts import render

# Create your views here.
class BlogView:

    def index(request):
        return render(request, 'blog/index.html')
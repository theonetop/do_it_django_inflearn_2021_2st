from django.shortcuts import render
from .models import Post

posts = Post.objects.all().order_by("-pk")

# Create your views here.
def index(request):
    return render(
        request,
        "blog/index.html",      # templates 
        {
            "posts" : posts
        }
    )
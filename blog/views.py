from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class PostList(ListView):
    model = Post
    # template_name = "blog/index.html"
    ordering = "-pk"
    

class PostDetail(DetailView):
    model = Post
    # template_name = "blog/single_page.html"

# # Create your views here.
# def index(request):
#     posts = Post.objects.all().order_by("-pk")
    
#     return render(
#         request,
#         "blog/index.html",      # templates 
#         {
#             "posts" : posts
#         }
#     )
    
# def single_page_post(request, pk):
#     post = Post.objects.get(pk=pk)
    
#     return render(
#         request,
#         "blog/single_page.html",
#         {
#             "post": post
#         }
#     )
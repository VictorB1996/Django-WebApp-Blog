from time import time
from typing import List
from django.http import request
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import DeleteView
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils import timezone
from datetime import datetime
# from django.http import HttpResponse

# def home(request):
#     context = {
#         "posts": Post.objects.all()
#     }
#     return render(request, "blog/home.html", context)

class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]
    paginate_by = 5


class RecentPostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(date_posted__date = datetime.today().date()).order_by("-date_posted").all()


class UserPostListView(ListView):
    model = Post
    template_name = "blog/user_posts.html"
    context_object_name = "posts"
    # ordering = ["-date_posted"]
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get("username"))
        return Post.objects.filter(author = user).order_by("-date_posted")
        

class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"

    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        current_post = self.get_object()
        if self.request.user == current_post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    context_object_name = "post"
    success_url = "/"

    def test_func(self):
        current_post = self.get_object()
        if self.request.user == current_post.author:
            return True
        return False

def search_posts(request):
    if request.method == "POST":
        searched = request.POST["search-bar"]
        posts = Post.objects.filter(title__contains = searched)
    
    return render(request, "blog/home.html", {"searched" : searched, "posts": posts})

def about(request):
    return render(request, "blog/about.html", {"title": "About"})



# def recent_posts(request):
#     context = {
#         "posts": Post.objects.filter(date_posted__date = datetime.today().date()).all()
#     }
#     return render(request, "blog/home.html", context)
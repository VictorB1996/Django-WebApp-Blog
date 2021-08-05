from django.urls import path
from django.views.generic.edit import CreateView
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, RecentPostListView, UserPostListView

urlpatterns = [
    path("", view = PostListView.as_view(), name = "blog-home"),
    # path("recent/", view = views.recent_posts, name = "recent-posts"),
    path("recent/", RecentPostListView.as_view(), name = "recent-posts"),
    path("user/<str:username>", UserPostListView.as_view(), name = "user-posts"),
    path("post/<int:pk>/", PostDetailView.as_view(), name = "post-detail"),
    path("post/<int:pk>/update", PostUpdateView.as_view(), name = "post-update"),
    path("post/<int:pk>/delete", PostDeleteView.as_view(), name = "post-delete"),
    path("post/new/", PostCreateView.as_view(), name = "post-create"),
    path("about/", view = views.about, name = "blog-about"),
    path("search_posts/", views.search_posts, name = "search-posts")
]


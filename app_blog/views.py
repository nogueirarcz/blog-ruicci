from django.views.generic import DetailView, ListView
from .models import Post


class PostListView(DetailView):

    model = Post


class PostDetailView(DetailView):

    model = Post
    
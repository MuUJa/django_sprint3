from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Post, Location, Category


class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    queryset = Post.published.order_by('-pub_date')[:5]


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        return Post.published.get_object_or_404(pk=self.kwargs['pk'])


class CategoryView(ListView):
    model = Post
    template_name = 'blog/category.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        category = get_object_or_404(
            Category, slug=self.kwargs['slug'], is_published=True)
        return Post.published.filter(category=category).order_by('-pub_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(
            Category, slug=self.kwargs['slug'])
        return context

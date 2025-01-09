from django.shortcuts import render

posts = list()
posts_dict = dict()

def index(request):
    template = 'blog/index.html'
    context = {'posts': reversed(posts)}
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    context = {'post': posts_dict[id]}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    context = {'category_slug': category_slug}
    return render(request, template, context)

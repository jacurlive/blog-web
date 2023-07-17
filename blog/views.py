from django.views.generic import ListView, DetailView

from blog.models import About, Blog


class MainView(ListView):
    template_name = 'blog/index.html'
    queryset = About.objects.first()
    context_object_name = 'about'


class AboutView(ListView):
    template_name = 'blog/about.html'
    queryset = About.objects.first()
    context_object_name = 'about'


class BlogView(ListView):
    template_name = 'blog/blog.html'
    queryset = Blog.objects.order_by('-created_at')
    context_object_name = 'blogs'


class BlogDetailView(DetailView):
    template_name = 'blog/blog_detail.html'
    query_pk_and_slug = 'slug'
    queryset = Blog.objects.all()
    context_object_name = 'post'

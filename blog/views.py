from django.views.generic import ListView, DetailView, View
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from blog.models import About, Blog
from .forms import BlogForm


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


class AddPostView(View):
    def get(self, request):
        if request.user.username == 'admin':
            form = BlogForm()
            context = {
                "form": form
            }
            return render(request, "blog/add_post.html", context)
        else:
            return HttpResponseRedirect("/")
    
    def post(self, request):
        if request.user.username == "admin":
            form = BlogForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/blog")
            else:
                return HttpResponse("error: post not added")
        else:
            return HttpResponseRedirect("/")

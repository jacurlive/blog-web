from django.urls import path

from blog.views import MainView, AboutView, BlogView, BlogDetailView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('about', AboutView.as_view(), name='about'),
    path('blog', BlogView.as_view(), name='blog'),
    path('blog/<str:slug>', BlogDetailView.as_view(), name='post')
]

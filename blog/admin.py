from django.contrib import admin
from django.contrib.admin import ModelAdmin
from blog.models import About, Blog


@admin.register(About)
class AboutAdmin(ModelAdmin):
    fields = ('full_name', 'image', 'specialization', 'instagram_link', 'github_link', 'linkedin_link', 'telegram_link',
              'short_bio', 'bio')
    list_display = ('id', 'full_name', 'specialization', 'short_bio')


@admin.register(Blog)
class BlogAdmin(ModelAdmin):
    fields = ('title', 'main_image', 'content')
    list_display = ('title', 'created_at')

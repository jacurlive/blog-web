from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django_summernote.admin import SummernoteModelAdmin
from blog.models import About, Blog


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    fields = ('full_name', 'image', 'specialization', 'instagram_link', 'github_link', 'linkedin_link', 'telegram_link',
              'short_bio', 'bio')
    list_display = ('id', 'full_name', 'specialization', 'short_bio')



class BlogAdmin(SummernoteModelAdmin):
    fields = ('title', 'content')
    list_display = ('title', 'created_at')


admin.site.register(Blog, BlogAdmin)

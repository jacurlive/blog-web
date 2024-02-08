from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title", "content"]

    content = forms.CharField(widget=SummernoteWidget)

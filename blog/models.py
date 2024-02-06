from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models import Model, CharField, URLField, TextField, DateTimeField, SlugField, ImageField
from django.utils.text import slugify


class About(Model):
    full_name = CharField(max_length=300)
    specialization = CharField(max_length=255)
    image = ImageField(upload_to='about/', default=None, blank=True)
    instagram_link = URLField()
    github_link = URLField()
    linkedin_link = URLField()
    telegram_link = URLField()
    short_bio = TextField()
    bio = RichTextUploadingField()


class Blog(Model):
    title = CharField(max_length=255)
    main_image = ImageField(upload_to='posts/', default=None, blank=True)
    content = RichTextField()
    created_at = DateTimeField(auto_now_add=True)
    slug = SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        while Blog.objects.filter(slug=self.slug).exists():
            slug = Blog.objects.filter(slug=self.slug).first().slug
            if '-' in slug:
                try:
                    if slug.split('-')[-1] in self.title:
                        self.slug += '-1'
                    else:
                        self.slug = '-'.join(slug.split('-')[:-1]) + '-' + str(int(slug.split('-')[-1]) + 1)
                except Exception as e:
                    self.slug = slug + '-1'
            else:
                self.slug += '-1'

        super().save(*args, **kwargs)

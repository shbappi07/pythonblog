from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager

# Create your models here.

class Blog(models.Model):
    blog_name = models.CharField(max_length=200)
    details = models.CharField(max_length=200)

    def __str__(self):
        return self.blog_name

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank= True)
    description = RichTextUploadingField()
    featured_image = models.ImageField(upload_to='uploads/')
    tags = TaggableManager(blank= True)
    featured = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now=True)
    mod_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



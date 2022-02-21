from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
      

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    published = models.DateTimeField(default=now)
    image = models.ImageField(upload_to="blog", null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, related_name="get_posts")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
      

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

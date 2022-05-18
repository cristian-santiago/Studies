from re import T
from ssl import create_default_context
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model): #Posts from blog site
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

# This class order the most recent post to last
    class Meta:
        ordering = ('-created',)

#This fuction change the name of posts object on the site, it change to title
    def __str__(self):
        return self.title
        
# This function will get the right url for any slug
    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={'slug': self.slug})

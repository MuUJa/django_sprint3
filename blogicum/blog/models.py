from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Location(models.Model):
    name = models.CharField(max_length=256)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    pub_date = models.DateTimeField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts"
    )
    location = models.ForeignKey(
        Location, null=True, blank=True,
        on_delete=models.SET_NULL, related_name="posts"
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name="posts"
    )
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

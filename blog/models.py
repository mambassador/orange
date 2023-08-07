from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="images/user", null=True, blank=True)

    def __str__(self):
        return self.get_full_name()


class Post(models.Model):
    title = models.CharField(max_length=70)
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    is_published = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    photo = models.ImageField(upload_to="images/post", null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=120)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=250)
    pub_date = models.DateField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

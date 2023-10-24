from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
import os

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, password=password)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(username=username, email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    REQUIRED_FIELDS = ['email']

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()

    def __str__(self):
        return self.title
    
    verbose_name_plural = 'Categories'


def get_upload_path(instance, filename):
    subdirectory = 'uploads/'

    return os.path.join(subdirectory, filename)



class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    overview = models.TextField()
    content =models.TextField()
    author = models.ForeignKey('blog.User', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    thumbnail = models.ImageField(upload_to=get_upload_path, blank=True, null=True)
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()
    likes = models.IntegerField(default=0)

    def likes_increment(self):
        self.likes += 1
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

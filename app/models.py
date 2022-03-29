from django.db.models.signals import post_save
from django.db.models.fields import URLField
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db import models
import datetime


# GENDERS
class Genders(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


# REVIEW⭐
class Review(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


# ENTRIES
class Entries(models.Model):
    title = models.CharField(max_length=30, unique=True, null=True)
    description = models.CharField(max_length=35, unique=True, null=True)
    content = models.TextField(unique=True)
    article = models.TextField(unique=True, null=True)
    gender = models.ForeignKey(Genders, on_delete=models.PROTECT)
    review = models.ForeignKey(Review, on_delete=models.PROTECT)
    url = URLField(blank=True)
    date = models.DateField(datetime.date.today)
    image = models.ImageField(upload_to="app.images")
    miniature = models.ImageField(upload_to="app.images_miniature")

    def __str__(self):
        return self.title


# NEWS
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    number = models.IntegerField(unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=75, unique=True)
    content = models.TextField()
    copiri = models.CharField(max_length=75, unique=True, null=True)
    url = URLField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="app.images")

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title


# GAMES
class Game(models.Model):
    title = models.CharField(max_length=50, unique=True)
    gender = models.ForeignKey(Genders, on_delete=models.PROTECT)
    gb = models.IntegerField(null=True)
    description = models.CharField(max_length=35, unique=True, null=True)
    content = models.TextField(unique=True)
    requirement = models.CharField(max_length=2, null=True)
    requirementm = models.TextField(unique=True, null=True)
    requirementr = models.TextField(unique=True, null=True)
    screen1 = URLField(blank=True, null=True)
    screen2 = URLField(blank=True, null=True)
    screen3 = URLField(blank=True, null=True)
    download1 = URLField(blank=True, null=True)
    download2 = URLField(blank=True, null=True)
    download3 = URLField(blank=True, null=True)
    review = models.ForeignKey(Review, on_delete=models.PROTECT)
    date = models.DateField(datetime.date.today)
    url = URLField(blank=True)
    image = models.ImageField(upload_to="app.images")
    miniature = models.ImageField(upload_to="app.miniature")

    def __str__(self):
        return self.title


# COMMENTS
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return "Comment {} by {}".format(self.body, self.name)


# ASIDE
class Aside(models.Model):
    header = models.CharField(max_length=30, unique=True)
    note = models.TextField(unique=True)
    photo = models.ImageField(upload_to="app.images")
    link = URLField(blank=True)


# PROFILES
def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return "profiles/" + filename


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ["user__username"]


@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get("created", False):
        Profile.objects.get_or_create(user=instance)

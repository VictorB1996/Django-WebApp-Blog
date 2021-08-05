from django.db import models
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    # auto_now_add = True # Set the date posted to the current datetime only when the object is created
    date_posted = models.DateTimeField(default = timezone.now) 
    # One to many relationship: one user can have multiple posts, but one post belongs only to one user
    # on_delete: What happens if we delete the user?
    # on_delete = models.CASCADE - when the user is deleted, the post gets deleted as well
    author = models.ForeignKey(User, on_delete = models.CASCADE) 

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs = {'pk': self.pk})

from calendar import month
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User
from django.db import models
# from datetime import datetime,date

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    profile_photo = models.CharField(max_length=1000)


class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    photo = models.CharField(max_length=1000)
    caption = models.CharField(max_length=1000)


from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)

class Course(models.Model):
    title = models.CharField(max_length=200)
    users = models.ManyToManyField(User, related_name='studiORM')

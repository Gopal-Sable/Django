# artistapp/models.py

from django.contrib.auth.models import User
from django.db import models

class Work(models.Model):
    LINK_CHOICES = (
        ('YT', 'Youtube'),
        ('IG', 'Instagram'),
        ('OT', 'Other'),
    )

    link = models.CharField(max_length=255)
    work_type = models.CharField(max_length=2, choices=LINK_CHOICES)

    def __str__(self):
        return self.link

class Artist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    works = models.ManyToManyField(Work)

    def __str__(self):
        return self.name

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Movie(models.Model):
    title=models.CharField(max_length=200)
    director=models.CharField(max_length=100)
    genre=models.CharField(max_length=100)
    release_date=models.DateField()
    description=models.TextField()
    poster=models.ImageField(upload_to='posters/',blank=True,null=True)

    def __str__(self):
        return self.title

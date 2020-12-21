from django.db import models


class Musician(models.Model):
    author = models.CharField('author', max_length=100)
    song = models.CharField('song', max_length=100)
    position = models.PositiveBigIntegerField(unique=True)


# Create your models here.

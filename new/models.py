from django.db import models

# Create your models here.


class New(models.Model):
    char = models.CharField(max_length=255)
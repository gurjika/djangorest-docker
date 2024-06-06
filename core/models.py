from django.db import models
from django.utils import timezone
# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

class Book(models.Model):
    title = models.CharField(max_length=255)
    year_published = models.DateField(default=timezone.now)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
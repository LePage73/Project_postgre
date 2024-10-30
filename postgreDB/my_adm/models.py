from django.db import models
from django.utils import timezone


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    create_date = models.DateTimeField(default=timezone.now())
    content = models.TextField()
    author = models.ForeignKey(Author, null=True, on_delete=models.PROTECT)
    def __str__(self):
        return self.title

class Bookshop(models.Model):
    name = models.TextField(default='название')
    adress = models.TextField(default='адрес')
    def __str__(self):
        return self.name
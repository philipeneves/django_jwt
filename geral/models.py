from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'book'
        ordering = ['title']

    def __str__(self):
        return self.title

class BookUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    book = models.ForeignKey('Book', on_delete=models.PROTECT)
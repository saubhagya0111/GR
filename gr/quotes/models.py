from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(null=True, blank=True)

class Quote(models.Model):
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.CharField(max_length=200, null=True, blank=True)

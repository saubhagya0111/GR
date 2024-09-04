from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Quote(models.Model):
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, null=True, blank=True, on_delete=models.SET_NULL)
    genre = models.ManyToManyField(Genre)  # A quote can have multiple genres

    def __str__(self):
        return self.text[:50]  # Display first 50 characters of the quote

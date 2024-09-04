from django.contrib import admin
from .models import Quote, Author, Book, Genre

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'get_books', 'get_genres')
    search_fields = ('text', 'author__name', 'book__title')
    list_filter = ('author', 'book', 'genre')

    def get_books(self, obj):
        return obj.book.title if obj.book else "No book"
    get_books.short_description = 'Book'

    def get_genres(self, obj):
        return ", ".join([genre.name for genre in obj.genre.all()])
    get_genres.short_description = 'Genres'

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    search_fields = ('title', 'author__name')
    list_filter = ('author',)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

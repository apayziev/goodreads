from django.contrib import admin
from books.models import Book, Author, BookReview
from users.models import CustomUser
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'isbn', 'description')
    list_filter = ('title', 'isbn', 'description')
    search_fields = ('title', 'isbn', 'description')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    list_filter = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')


class BookReviewAdmin(admin.ModelAdmin):
    list_display = ('comment', 'rating', 'book', 'user')
    list_filter = ('comment', 'rating', 'book', 'user')
    search_fields = ('comment', 'rating', 'book', 'user')


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(BookReview, BookReviewAdmin)
admin.site.register(CustomUser)

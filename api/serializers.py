from books.models import Book, BookReview, Author
from rest_framework import serializers
from users.models import CustomUser


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'description', 'isbn', 'cover_pic')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name', 'email', 'bio')


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'first_name',
                  'last_name', 'email', 'profile_pic')


class BookReviewSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    book = BookSerializer(read_only=True)

    user_id = serializers.IntegerField(write_only=True)
    book_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = BookReview
        fields = ('id', 'comment', 'rating', 'created_at',
                  'book', 'user', 'user_id', 'book_id')

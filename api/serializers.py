from books.models import Book, BookReview
from rest_framework import serializers
from users.models import CustomUser


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'description', 'isbn', 'cover_pic')


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'first_name',
                  'last_name', 'email', 'profile_pic')


class BookReviewSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    book = BookSerializer()

    class Meta:
        model = BookReview
        fields = ('id', 'comment', 'rating', 'created_at', 'book', 'user')

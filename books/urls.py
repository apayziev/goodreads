from django.urls import path
from .views import BooksListView, BooksDetailView, AddReviewView

app_name = 'books'

urlpatterns = [
    path('books_list', BooksListView.as_view(), name='books_list'),
    path('book_detail/<int:book_id>',
         BooksDetailView.as_view(), name='book_detail'),
    path('add_review/<int:book_id>',
         AddReviewView.as_view(), name='add_review'),
]

from django.urls import path
from .views import BooksListView, BooksDetailView, AddReviewView, \
    EditReviewView, ConfirmDeleteReviewView, DeleteReviewView

app_name = 'books'

urlpatterns = [
    path('books_list', BooksListView.as_view(), name='books_list'),
    path('book_detail/<int:book_id>',
         BooksDetailView.as_view(), name='book_detail'),
    path('add_review/<int:book_id>',
         AddReviewView.as_view(), name='add_review'),
    path('edit_review/<int:book_id>/<int:review_id>',
         EditReviewView.as_view(), name='edit_review'),
    path('confirm_delete_review/<int:book_id>/<int:review_id>',
         ConfirmDeleteReviewView.as_view(), name='confirm_delete_review'),
    path('delete_review/<int:book_id>/<int:review_id>',
         DeleteReviewView.as_view(), name='delete_review'),
]

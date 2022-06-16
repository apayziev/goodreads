from django.urls import path
from api.views import BookReviewDetailAPIView, BookListAPIView

app_name = 'api'

urlpatterns = [
    path('book_review/<int:pk>',
         BookReviewDetailAPIView.as_view(), name='review_detail'),
    path('book_reviews/', BookListAPIView.as_view(), name='review_list'),
]

from django.urls import path
# from api.views import BookReviewDetailAPIView, BookListAPIView
from rest_framework.routers import DefaultRouter
from api.views import BookReviewsViewSet, BookViewSet, AuthorViewSet



app_name = 'api'

router = DefaultRouter()
router.register(r'reviews', BookReviewsViewSet, basename='reviews')
router.register(r'books', BookViewSet, basename='books')
router.register(r'authors', AuthorViewSet, basename='authors')


urlpatterns = router.urls

# urlpatterns = [
#     path('book_review/<int:pk>',
#          BookReviewDetailAPIView.as_view(), name='review_detail'),
#     path('book_reviews/', BookListAPIView.as_view(), name='review_list'),
# ]

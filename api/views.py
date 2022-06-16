from rest_framework.response import Response
from rest_framework.views import APIView
from books.models import BookReview
from api.serializers import BookReviewSerializer

# Create your views here.


class BookReviewDetailAPIView(APIView):
    def get(self, request, pk):
        book_review = BookReview.objects.get(pk=pk)
        serializer = BookReviewSerializer(book_review)

        return Response(data=serializer.data)


class BookListAPIView(APIView):
    def get(self, request):
        book_reviews = BookReview.objects.all()
        serializer = BookReviewSerializer(book_reviews, many=True)

        return Response(data=serializer.data)

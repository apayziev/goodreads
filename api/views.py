# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.pagination import PageNumberPagination
# from rest_framework import status
# from rest_framework import generics
from rest_framework import viewsets
from books.models import Book, BookReview, Author
from api.serializers import AuthorSerializer, BookReviewSerializer, BookSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class BookReviewsViewSet(viewsets.ModelViewSet):
    queryset = BookReview.objects.all().order_by('-created_at')
    serializer_class = BookReviewSerializer

    permission_classes = [IsAuthenticated]


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    permission_classes = [IsAuthenticated]


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    permission_classes = [IsAuthenticated]


# class BookReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthenticated]

#     queryset = BookReview.objects.all()
#     serializer_class = BookReviewSerializer
#     lookup_field = 'pk'

    # def get(self, request, pk):
    #     book_review = BookReview.objects.get(pk=pk)
    #     serializer = BookReviewSerializer(book_review)

    #     return Response(data=serializer.data)

    # def put(self, request, pk):
    #     book_review = BookReview.objects.get(pk=pk)
    #     serializer = BookReviewSerializer(book_review, data=request.data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(data=serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def patch(self, request, pk):
    #     book_review = BookReview.objects.get(pk=pk)
    #     serializer = BookReviewSerializer(
    #         book_review, data=request.data, partial=True)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(data=serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk):
    #     book_review = BookReview.objects.get(pk=pk)
    #     book_review.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


# class BookListAPIView(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticated]

#     queryset = BookReview.objects.all().order_by('-created_at')
#     serializer_class = BookReviewSerializer
#     pagination_class = PageNumberPagination

    # def get(self, request):
    #     book_reviews = BookReview.objects.all().order_by('-created_at')

    #     paginator = PageNumberPagination()

    #     page_obj = paginator.paginate_queryset(book_reviews, request)

    #     serializer = BookReviewSerializer(page_obj, many=True)

    #     return paginator.get_paginated_response(serializer.data)

    # def post(self, request):
    #     serializer = BookReviewSerializer(data=request.data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)

    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

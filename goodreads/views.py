from django.shortcuts import render

from books.models import BookReview

# Create your views here.


def landing_page(request):
    return render(request, 'landing_page.html')


def home_page(request):
    book_reviews = BookReview.objects.all().order_by('-created_at')
    return render(request, 'home_page.html', {'book_reviews': book_reviews})

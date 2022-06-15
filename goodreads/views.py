from django.shortcuts import render
from django.core.paginator import Paginator

from books.models import BookReview

# Create your views here.


def landing_page(request):
    return render(request, 'landing_page.html')


def home_page(request):
    book_reviews = BookReview.objects.all().order_by('-created_at')
    page_size = request.GET.get('page_size', 3)
    paginator = Paginator(book_reviews, page_size)

    page_number = request.GET.get('page', 1)
    page_ojbect = paginator.get_page(page_number)

    return render(request, 'home_page.html', {'page_obj': page_ojbect})

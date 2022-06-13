from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import ListView, DetailView
from books.forms import BookReviewForm
from books.models import Book, BookReview
# Create your views here.


# class BooksListView(View):
#     def get(self, request):
#         books = Book.objects.all()
#         context = {
#             'books': books
#         }
#         return render(request, 'books/books_list.html', context=context)

class BooksListView(ListView):
    template_name = 'books/books_list.html'
    queryset = Book.objects.all()
    context_object_name = 'books'
    paginate_by = 2

    def get_queryset(self):
        search_query = self.request.GET.get('q')
        if search_query:
            return self.queryset.filter(title__icontains=search_query)
        return self.queryset


class BooksDetailView(View):
    def get(self, request, book_id):
        book = Book.objects.get(id=book_id)
        review_form = BookReviewForm()

        context = {
            'book': book,
            'review_form': review_form
        }
        return render(request, 'books/book_detail.html', context=context)


class AddReviewView(LoginRequiredMixin, View):
    def post(self, request, book_id):
        book = Book.objects.get(id=book_id)
        review_form = BookReviewForm(data=request.POST)

        if review_form.is_valid():
            BookReview.objects.create(
                user=request.user,
                book=book,
                comment=review_form.cleaned_data['comment'],
                rating=review_form.cleaned_data['rating']
            )
            return redirect('books:book_detail', book_id=book_id)

        else:
            context = {
                'book': book,
                'review_form': review_form
            }
            return render(request, 'books/book_detail.html', context=context)


# class BooksDetailView(DetailView):
#     template_name = 'books/book_detail.html'
#     pk_url_kwarg = 'book_id'
#     context_object_name = 'book'
#     model = Book
#     form_class = BookReviewForm

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['review_form'] = self.form_class
#         return context

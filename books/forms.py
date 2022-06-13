from django import forms

from books.models import BookReview


class BookReviewForm(forms.ModelForm):
    class Meta:
        model = BookReview
        fields = ('comment', 'rating')
        widgets = {
            'comment': forms.Textarea(attrs={'placeholder': 'Write your review here ...', 'rows': '3', 'cols': '50'}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5})
        }

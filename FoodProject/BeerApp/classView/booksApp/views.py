from django.views.generic import ListView, DetailView
from booksApp.models import Book
# Create your views here.
#implementing ListView comming from django.views.generic
class BookListView(ListView):
    #model for which list view is required
    model = Book

#DetailView class
class BookDetailView(DetailView):
    #model for Detail view
    model = Book

    template_name = 'booksApp/book_detail.html'


from django.urls import path
from booksApp.views import BookListView, BookDetailView
urlpatterns = [
    path('', BookListView.as_view()),
    path('details/<pk>',BookDetailView.as_view())

]

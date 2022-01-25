from django.contrib import admin
from booksApp.models import Book
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ['title','author','pages','price']
#regsitering the book on admin panel
admin.site.register(Book,BookAdmin)

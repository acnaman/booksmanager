from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.
def index(request):
    book_list = Book.objects.order_by('title')
    context = {'book_list': book_list}
    return render(request, 'books/index.html', context)

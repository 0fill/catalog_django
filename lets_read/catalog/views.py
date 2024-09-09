from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Book
from .forms import BookForm


# Create your views here.

def home(request):
    return render(request, 'home.html')


def all_books(request):
    books = Book.objects.all().values()
    context = {'books': books}
    return render(request, 'all_books.html', context)


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("library")
    return render(request, "add_book.html", {'form': BookForm()})


def detail_book(request, name):
    book = Book.objects.get(name=name)
    context = {'book': book}
    return render(request, 'detail.html', context)

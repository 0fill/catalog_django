from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from .models import Book
from .forms import BookForm,UserRegistrationForm


# Create your views here.

class BookListView(ListView):
    model = Book
    template_name = 'all_books.html'


class BookDetailView(DetailView):
    model = Book
    template_name = 'detail.html'


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'add_book.html'
    success_url = reverse_lazy('library')
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

@login_required
def profile_page(request):
    return render(request, 'profile.html')


def register_page(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request,
                  'register.html',
                  {'form': UserRegistrationForm()})


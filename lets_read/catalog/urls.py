from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('library/', views.all_books, name='library'),
    path('library/add_book', views.add_book, name='add_book'),
    ]

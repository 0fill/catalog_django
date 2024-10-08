from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('library/', BookListView.as_view(), name='library'),
    path('library/add_book', BookCreateView.as_view(), name='add_book'),
    path("book_detail/<int:pk>/", BookDetailView.as_view(), name='deatil_book'),
    path('accounts/profile/', profile_page, name="profile"),
    path('register/', register_page, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    ]

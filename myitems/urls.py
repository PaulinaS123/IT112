from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.get_all_books, name='get_all_books'),
    path('book/', views.get_single_book, name='get_single_book'),
    path('book/add/', views.add_book, name='add_book'),
]

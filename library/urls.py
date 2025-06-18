from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('<int:book_id>/', views.book_detail, name='book_detail'),


    # API views for assignment
    path('api/books/', views.get_all_books),
    path('api/book/', views.get_single_book),
    path('api/books/add/', views.add_book),
]

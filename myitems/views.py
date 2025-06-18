from django.shortcuts import render

import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from .models import Book


def get_all_books(request):
    if request.method == 'GET':
        books = Book.objects.all().values('id', 'title', 'author', 'genre')
        books_list = list(books)
        return JsonResponse(books_list, safe=False, content_type='application/json')
    else:
        return HttpResponseBadRequest('Invalid HTTP method')


def get_single_book(request):
    if request.method == 'GET':
        book_id = request.GET.get('id')
        if not book_id:
            return JsonResponse({'error': 'Missing id parameter'}, status=400)
        try:
            book = Book.objects.values(
                'id', 'title', 'author', 'genre').get(id=book_id)
            return JsonResponse(book, content_type='application/json')
        except Book.DoesNotExist:
            return JsonResponse({'error': 'Book not found'}, status=404)
    else:
        return HttpResponseBadRequest('Invalid HTTP method')


@csrf_exempt
def add_book(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            title = data.get('title')
            author = data.get('author')
            genre = data.get('genre')
            if not title or not author or not genre:
                return JsonResponse({'error': 'Missing title, author or genre'}, status=400)

            book = Book.objects.create(title=title, author=author, genre=genre)
            return JsonResponse({'success': True, 'book_id': book.id}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return HttpResponseBadRequest('Invalid HTTP method')

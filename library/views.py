from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Book


def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'library/book_detail.html', {'book': book})


# ➕ New API views for the assignment

def get_all_books(request):
    books = list(Book.objects.values())
    return JsonResponse(books, safe=False, content_type="application/json")


def get_single_book(request):
    book_id = request.GET.get('id')
    if book_id:
        try:
            book = Book.objects.get(id=book_id)
            return JsonResponse({
                'id': book.id,
                'title': book.title,
                'author': book.author,
                'genre': book.genre
            }, content_type="application/json")
        except Book.DoesNotExist:
            return JsonResponse({'error': 'Book not found'}, content_type="application/json")
    return JsonResponse({'error': 'No ID provided'}, content_type="application/json")


def add_book(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            book = Book.objects.create(
                title=data['title'],
                author=data['author'],
                genre=data['genre']
            )
            return JsonResponse({
                'success': True,
                'message': 'Book added successfully',
                'book_id': book.id
            }, content_type="application/json")
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, content_type="application/json")
    return JsonResponse({'success': False, 'error': 'Only POST method allowed'}, content_type="application/json")

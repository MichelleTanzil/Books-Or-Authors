from django.shortcuts import render, redirect
from .models import Book, Author

# Home Page with books
def index(request):
    context = {
        "all_the_books": Book.objects.all(),
        "all_the_authors": Author.objects.all(),
    }
    return render(request, 'main_app/index.html', context)

# Add book on home page
def add_book(request):
    Book.objects.create(
        title=request.POST['title'], desc=request.POST['description'])
    return redirect('/')

# Book profile
def book_profile(request, book_id):
    book_in_question = Book.objects.get(id=book_id)
    context = {
        "book": book_in_question,
        "authors_excluded": Author.objects.exclude(books=book_in_question),
    }
    return render(request, 'main_app/book_profile.html', context)

# Add author to book in book profile
def add_author(request, book_id):
    book = Book.objects.get(id=book_id)
    author_id = request.POST['author']
    author = Author.objects.get(id=author_id)
    book.authors.add(author)
    return redirect(f"/books/{book_id}")


# Author home page
def authors_summary(request):
    context = {
        "all_the_books": Book.objects.all(),
        "all_the_authors": Author.objects.all(),
    }
    return render(request, 'main_app/authors_summary.html', context)

# Add author to author home page
def add_author_summary(request):
    Author.objects.create(
        first_name=request.POST['first_name'], last_name=request.POST['last_name'], notes=request.POST['notes'])
    return redirect('/author')

# Author profile page
def author_profile(request, author_id):
    author_in_question = Author.objects.get(id=author_id)
    context = {
        "author": author_in_question,
        "books_excluded": Book.objects.exclude(authors=author_in_question),
    }

    return render(request, 'main_app/author_profile.html', context)

# Add book to author in author profile page
def add_book_to_author(request, author_id):
    book_id = request.POST['books']
    book = Book.objects.get(id=book_id)
    author = Author.objects.get(id=author_id)
    author.books.add(book)
    return redirect(f"/author/{author.id}")

from django.shortcuts import render, redirect
from .models import *

def books(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, "books_authors_app/books.html", context)

def add_book(request):
    new_book = Book.objects.create(title=request.POST['new_title'], desc=request.POST['new_desc'])
    return redirect("/books/"+str(new_book.id))

def show_book(request, b_id):
    # print(Book.objects.get(id=b_id).authors.values())
    print(Book.objects.get(id=b_id).desc)
    print('*'*85)
    context = {
        'book': Book.objects.get(id=b_id),
        'authors': Book.objects.get(id=b_id).authors.values(),
        'auth_to_add': Book.auth_not_on_book(b_id)
    }
    return render(request, "books_authors_app/books_edit.html", context)


#function to add a new author to a book
#calls the book, then adds the author to it
def book_add_auth(request):
    Book.objects.get(id=request.POST['book_id']).authors.add(Author.objects.get(id=request.POST['auth_to_add']))
    return redirect("/books/"+str(request.POST['book_id']))

def authors(request):
    context = {
        'authors':Author.objects.all()
    }
    return render(request, "books_authors_app/authors.html", context)

def add_author(request):
    new_auth = Author.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], notes=request.POST['notes'])
    printhelper(new_auth)
    return redirect("/authors/"+str(new_auth.id))

def show_author(request, a_id):
    context = {
        'author': Author.objects.get(id=a_id),
        'books': Author.objects.get(id=a_id).books.values(),
        'book_to_add': Author.book_not_by_auth(a_id)
    }
    return render(request, "books_authors_app/authors_edit.html", context)

def auth_add_book(request):
    Book.objects.get(id=request.POST['book_id']).authors.add(Author.objects.get(id=request.POST['auth_to_add']))
    return redirect("/authors/"+str(request.POST['auth_to_add']))

def printhelper(val):
    print('*'*80)
    print(val)
    print('*'*80)



# Create your views here.

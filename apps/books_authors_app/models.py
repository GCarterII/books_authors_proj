from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def auth_not_on_book(b_id):
        book = Book.objects.get(id=b_id)
        authors = book.authors.values()
        a_list = []
        for author in authors:
            a_list.append(author['id'])
        all_authors = Author.objects.all().values()
        auth_list = []
        for auth in all_authors:
            if auth['id'] not in a_list:
                auth_list.append(auth)
        return auth_list



class Author(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    notes = models.TextField()
    books = models.ManyToManyField(Book, related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def book_not_by_auth(a_id):
        author = Author.objects.get(id=a_id)
        books = author.books.values()
        b_list = []
        for book in books:
            b_list.append(book['id'])
        all_books = Book.objects.all().values()
        book_list = []
        for book in all_books:
            if book['id'] not in b_list:
                book_list.append(book)
        return book_list





# Create your models here.

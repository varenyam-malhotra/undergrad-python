#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 13:06:31 2025

@author: vena
"""

class Book:
    def __init__(self, title, author, isbn, checked_out=False):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.checked_out = checked_out
        
    def check_out(self):
        self.checked_out = True
        return self.checked_out
    
    def check_in(self):
        self.checked_out = False
        return self.checked_out
    
class Member: 
    def __init__(self, member_id, name, checked_out_books = []): # want to initialize checked_out_books as an empty list
        self.member_id = member_id
        self.name = name
        self.checked_out_books = checked_out_books 
        
    def check_out_book(self, book : Book): # book must be of Class Book
        self.checked_out_books.append(book.title)
        
    def return_book(self, book : Book):
        self.checked_out_books.remove(book)
        
class Library:
    def __init__(self, books = []):
        self.books = books
        
    def add_books(self, book : Book):
        self.books.append(book.title)
        
    
        
if __name__ == "__main__":
    ## To check the Library class
    # Create a book instance
    book1 = Book("Python Programming", "John Smith", "978-1234567890")

    # Check out the book
    book1.check_out()

    # Check the book's status
    print(book1.checked_out)  # Expected output: True

    # Check in the book
    book1.check_in()

    # Check the book's status
    print(book1.checked_out)  # Expected output: False
    
    ## To check the Member class
    # Create a member instance
    member1 = Member("M001", "Alice")

    # Check out a book
    member1.check_out_book(book1)

    # Check the member's checked-out books
    print(member1.checked_out_books)  # Expected output: ["Python Programming"]

    # Return a book
    member1.return_book(book1)

    # Check the member's checked-out books
    print(member1.checked_out_books)  # Expected output: []
    
    
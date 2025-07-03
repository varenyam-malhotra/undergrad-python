#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 11:04:21 2024

@author: vena
"""

class Book:
    def __init__(self, title, author, isbn, checked_out):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.checked_out = checked_out
        
    def check_out(self, checked_out):
        self.checked_out = True
        
    def check_in(self, checked_out):
        self.checked_out = False
        
class Member(Book):
    def __init__(self, member_id, name, checked_out_books):
        self.member_id = member_id
        self.name = name
        self.checked_out_books = []
        
    def check_out_book(self):
        if not Book.checked_out():
            self.checked_out_books.append(self)
            
    def return_book(self):
        self.checked_out_books.pop(self)
        
class Library(Member):
    def __init__(self, books):
        self.books = []
    


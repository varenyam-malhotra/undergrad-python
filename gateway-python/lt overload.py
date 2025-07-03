# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Varenyam Malhotra
# 26 March, 2025

class Student:
    def __init__(self, name, age, graduation_year, gpa):
        self.name = name
        self.age = age
        self.graduation_year = graduation_year
        self.gpa = gpa
        
    def __lt__(self, other):
        if self.graduation_year != other.graduation_year:
            return self.graduation_year < other.graduation_year
        if self.gpa != other.gpa:
            return self.gpa > other.gpa
        if self.age != other.age:
            return self.age < other.age
        if self.name != other.name:
            return self.name < other.name
        
class Matrix:
    def __lt__(self, other):
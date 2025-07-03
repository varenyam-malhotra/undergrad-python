#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 11:04:28 2024

@author: vena
"""

class Student:
    def __init__(self, name, age, graduation_year, gpa):
        self.name = name
        self.age = age
        self.graduation_year = graduation_year
        self.gpa = gpa
        
    def __lt__(self, other):
        
        if self.graduation_year < other.graduation_year:
            less = self.graduation_year
        elif other.graduation_year < self.graduation_year:
            less = other.graduation_year
        elif self.graduation_year == other.graduation_year:
            if self.gpa > other.gpa:
                less = other.gpa
            elif self.gpa < other.gpa:
                less = self.gpa
            elif self.gpa = other.gpa:
                if self.age < other.age:
                    less = other.age
                elif self.age > other.age:
                    less = self.age
                elif self.age == other.age:
                    if self.name < other.name:
                        less = self.name
                    elif other.name < self.name:
                        less = other.name
                        
        return less
    
    def sorted_students(students):
        
    
if __name__ = "__main__":
    students = [
        Student("Alice", 22, 2023, 3.7),
        Student("Bob", 23, 2022, 3.8),
        Student("Carol", 21, 2023, 3.9),
        Student("David", 22, 2022, 3.8),
               ]
sorted_students = sorted(students)
for student in sorted_students: 
        print(f"{student.name}, Age: {student.age}, Graduation Year:{student.graduation_year}, GPA: {student.gpa}")
        
        
        
        
        
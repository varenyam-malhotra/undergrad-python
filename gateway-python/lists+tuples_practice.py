#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 16:42:11 2024

@author: vena
"""
"""
Write a Python program that does the following:

Create a list of tuples where each tuple contains the name of a student and their score on a quiz (you can add at least 5 students).
Use a loop to print out each student's name and score.
Sort the list of tuples in descending order based on the students' scores.
After sorting, print the name of the student with the highest score.
"""

student_scores = [("Johnny", 95), ("Akash", 97), ("Veronica", 98), ("Javier", 89), ("Cindy", 78)]
for x in student_scores:
    student, score = x
    print(f"Student: {student}, Score: {score}")
for i in range(0, len(student_scores)):
    print(student_scores[i])
    
sorted_students = sorted(student_scores, key=lambda x: x[0], reverse=True)
print(sorted_students)

student_1 = sorted_students[0]
name = student_1[0]
print(name)

print("--------")

for name, score in student_scores:
    if score > 90:
        print(name)








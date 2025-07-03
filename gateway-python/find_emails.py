#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 13:10:45 2025

@author: vena
"""

# Varenyam Malhotra
# 24 Feb 2025

# Sample text string
text = "Contact us at info@example.com or support@company.com for assistance."

def find_emails(text):
    text_list = text.split(" ")
    emails = []
    for i in text_list:
        if "@" in i:
            emails.append(i)
    return "\n".join(emails)
        
print(find_emails(text))
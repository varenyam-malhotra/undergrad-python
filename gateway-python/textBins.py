#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 11:11:25 2024

@author: vena
"""
# Varenyam Malhotra

# textBins program sept 25 2024 

def text2bin(text):
    """
    Converts text to binary string
    """
    binStr = ""
    for letter in text:
        binary = bin(ord(letter))[2:]
        pad    = 8 - len(binary)
        binStr += pad*'0' + binary
    return binStr

def bin2text(binStr):
    """
    Converts binary string to text
    """
    text = ""
    for i in range(0,len(binStr),8):
        text += chr(int(binStr[i:i+8],2))
    return text

print(text2bin("Varenyam"))

print(bin2text(text2bin("Hello")))

def dna2bin(dna):
    """
    Encodes DNA into a binary string 
    """
    dnaStr = ""
    for letter in dna:
        A = "00"
        T = "01"
        C = "10"
        G = "11"
        # Java way for string concatenation will not work
        binary = bin(ord(letter))[2:]
        pad    = 8 - len(binary)
        binStr += pad*'0' + binary
    return dnaStr

print(dna2bin("G"))
print(dna2bin("TAAT"))
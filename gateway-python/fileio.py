#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 11:24:53 2024

@author: vena
"""

"""
Examples for accessing files. 
"""

def writeYourFile():
    """
    Write text to file
    """
    
    yourText = "I like writing files.\nWriting files is fun!"
    
    with open("yourFile.txt","w") as yourFile:  # Open file in "w"rite mode
        print(yourText, file=yourFile)
        ### yourFile.write(yourText) # Another way to do this using write() method

def readYourFile():
    """"
    Read file and print each line one at time
    """
    
    with open("yourFile.txt","r") as yourFile: # Open file in "r"ead mode
        for line in yourFile: print(line)
        

def appendYourFile():
    """
    Append text to file.
    Unlike "w" mode which overwites the file, "a"ppend mode adds text to the end
    """
    
    yourText = "I've added another line"
    
    with open("yourFile.txt","a") as myFile:  #Open file in "a"ppend mode
        print(yourText, file=myFile) 


if __name__ == "__main__":

    writeYourFile()
    readYourFile()
    
    """
    appendYourFile()
    readYourFile()
    """

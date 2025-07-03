#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 19:56:03 2025

@author: vena
"""

import math
import inspect

"""
Note:
'filename' is a string representing the path to the file on disk.
'strFile' is a string containing the full text content of the file,
which is obtained by reading the file using the 'readFile' function.
The 'readFile' function takes a filename, opens the file, reads its content,
and returns it as a string (strFile). This string is then passed to other functions
(such as getTitle and getScalingFactor) for processing.

Good Luck!
"""

def readFile(filename):
    content=""
    with open(filename,"r") as fin:
        content=fin.read()
    return content

def getTitle(strFile):
    title=""
    return title

def getScalingFactor(strFile):
    sfactor=0.0
    return sfactor

def getElements(strFile):
    elements=[]
    return elements

def getNumElements(strFile):
    nelements=[]
    return nelements

def getAtomDecorations(strFile):
    decor=[]
    return decor

def parseStrFile(strFile):
    title=""
    elements=[]
    nelements=[]
    return title,elements,nelements

def getElementsNew(elements,element,replacement):
    elements_new=[]
    return elements_new

def getGCD(lst_int):
    _gcd=math.gcd(*lst_int)
    return _gcd

def getTitleNew(elements_new,nelements_reduced):
    title_new=""
    return title_new

def getReducedComposition(nelements):
    nelements_reduced=[]
    return nelements_reduced

def replaceAtomPositions(lines_new,nelements,elements_new,element,replacement):
    return lines_new

def replaceElement(strFile,element,replacement):
    strFile_new=""
    return strFile_new

def getPOCCTols(strFile):
    pocc_tols=[]
    return pocc_tols

def getNumElementsPOCC(strFile):
    nelements=[]
    occs=[]
    return nelements,occs

def coordsAreClose(coord1,coord2,tol):
    return True

def getPOCCSites(strFile):
    pocc_sites=[]
    return pocc_sites

def getNAtomsPOCC(strFile,supercell_size):
    natoms_ordered=0
    return natoms_ordered

def getAtomDecorationsPOCC(strFile,supercell_size):
    decor=[]
    return decor

def main():
    strFile=readFile("POSCAR_BiNNi2")
    print("getTitle()=",getTitle(strFile))
    strFile=readFile("PARTCAR_NPAg")
    print("getTitle()=",getTitle(strFile))


if __name__ == "__main__":
    main()

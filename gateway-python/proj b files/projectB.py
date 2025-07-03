#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 13:30:35 2024

@author: vena
"""

# Varenyam Malhotra
# Gateway Computing Python Project B

# -*- coding: utf-8 -*-
codons = {"UUU":"Phe", "UUC":"Phe", "UUA":"Leu", "UUG":"Leu",
          "UCU":"Ser", "UCC":"Ser", "UCA":"Ser", "UCG":"Ser",
          "UAU":"Tyr", "UAC":"Tyr", "UAA":"STOP", "UAG":"STOP",
          "UGU":"Cys", "UGC":"Cys", "UGA":"STOP", "UGG":"Trp",
          "CUU":"Leu", "CUC":"Leu", "CUA":"Leu", "CUG":"Leu",
          "CCU":"Pro", "CCC":"Pro", "CCA":"Pro", "CCG":"Pro",
          "CAU":"His", "CAC":"His", "CAA":"Gln", "CAG":"Gln",
          "CGU":"Arg", "CGC":"Arg", "CGA":"Arg", "CGG":"Arg",
          "AUU":"Ile", "AUC":"Ile", "AUA":"Ile", "AUG":"Met",
          "ACU":"Thr", "ACC":"Thr", "ACA":"Thr", "ACG":"Thr",
          "AAU":"Asn", "AAC":"Asn", "AAA":"Lys", "AAG":"Lys",
          "AGU":"Ser", "AGC":"Ser", "AGA":"Arg", "AGG":"Arg",
          "GUU":"Val", "GUC":"Val", "GUA":"Val", "GUG":"Val",
          "GCU":"Ala", "GCC":"Ala", "GCA":"Ala", "GCG":"Ala",
          "GAU":"Asp", "GAC":"Asp", "GAA":"Glu", "GAG":"Glu",
          "GGU":"Gly", "GGC":"Gly", "GGA":"Gly", "GGG":"Gly"}
        
def main():
    """ Simply runs a few essential functions in order to ensure the file runs
    Some of these functions include reading in the file containing DNA sequences
    Preparing using a list to print out the template string
    
    No parameters, no return: uses print statement to simply print template sequence using other functions in code
    """
    # Path to the file containing the DNA sequences

    file_paths = ["dna1.txt", "dna2.txt", "dna3.txt"]
    
    for i, file_path in enumerate(file_paths, start=1):
        sequences = readFile(file_path)
        
        reference_dna = sequences[0]
        subject_dna = sequences[1:]

        mutation_count = count(subject_dna[0], reference_dna)
        synonym_status = "synonymous" if synonymous(subject_dna, reference_dna) else "not synonymous"
        
        print(f"Subject {i} DNA has {mutation_count} mutations and is {synonym_status}")
   
    
def readFile(fileName):
    """
    Reads a text file.
    
    Parameters
    ----------
    fileName : str
        File path to read.

    Returns
    -------
    str
        Text from file.
    """
    with open(fileName,'r') as dnaFile:
        dna = "".join(dnaFile.readlines()).strip()
    return dna
    
    
def writeFile(fileName,text):
    """
    Writes a text file.

    Parameters
    ----------
    fileName : str
        File path to write.
    text : str
        Text to write.

    Returns
    -------
    None.

    """
    with open(fileName,'w') as textFile:
        textFile.write(text)
    
def transcribe(dna):
    """ Reads in DNA file and converts it into mRNA code
    Parameters: The DNA code (string)
    Returns: The mRNA code (string) """
    mRNA = ""
    for i in range(0, len(dna)):
        if dna[i] == "T":
            mRNA += "U"
        else: 
            mRNA += dna[i]
    return mRNA
    
print(transcribe("TAGACTGAGTA"))
 
   
def translate(mrna):
    """
    Translated an mRNA code of a, c, u, g into amino acids

    Parameters
    ----------
    mrna : string, genetic code

    Returns
    -------
    string of the first three letters of amino acids and continues on and on with the different amino acids

    """
    amino_acids = []
    for i in range(0, len(mrna), 3):
        codon = mrna[i: i+3]
        if codon in codons:
            amino_acids.append(codons[codon])
    return " ".join(amino_acids)

print(translate("GCUAUGUUUUAGGAA"))
    

def synonymous(sub, ref):
    """ sees if two differen mrna genetic codes end up being equivalent to the same string of amino acids 
    parameters: two mrna genetic codes: sub and ref
    returns: true or false boolean based on them equalling the same amino acid sequence or not
    """
    sub_amino_acids = translate(transcribe(sub))
    ref_amino_acids = translate(transcribe(ref))
    # Using translate and transcribe to convert a dna code into amino acid sequences
    if sub_amino_acids == ref_amino_acids:
        return True
    else:
        return False
    # Returning True or False

print(synonymous("ATTGTTGGG", "ATAGTAGGT"))


def delete(dna, i):
    """
    Deletes a base in the dna genetic code at index i

    Parameters
    ----------
    dna : string of dna genetic code
    i : an index position (of the dna genetic code)

    Returns
    -------
    deleted_dna : altered dna genetic code after the deletion

    """
    deleted_dna = dna[:i] + dna[i+1:]
    return deleted_dna

print(delete("ATCG", 2))


def insert(dna, i, base):
    """
    Inserts base at index position i into genetic code dna

    Parameters
    ----------
    dna : string dna genetic code
    i : int i position index
    base : string character A, G, T, or C to be inserted
    Returns
    -------
    inserted_dna : dna after insertion alteration

    """
    inserted_dna = dna[:i] + base
    inserted_dna = inserted_dna + dna[i:]
    return inserted_dna

print(insert("AAAA", 1, "C"))
print(insert("AAAA", 4, "C"))

def substitute(dna, i, base):
    """
    Substitutes base A, G, T, or C at position index i into dna genetic code

    Parameters
    ----------
    dna : string dna genetic code
    i : int i position index
    base : string character 'A', 'G', 'C', or 'T' to be substituted in the dna genetic code string 

    Returns
    -------
    substituted_dna : new string of dna genetic code after substituion alteration

    """
    substituted_dna = dna[:i] + base + dna[i+1:]
    return substituted_dna

print(substitute("ATTT", 1, "C"))

def diff(sub, ref):
    """returns position index of first difference between dna codes sub and ref 
    paramters are two genetic codes of dna: sub and ref
    returns a number integer for the first position index between the two genetic codes of dna strings"""
    min_len = min(len(sub), len(ref))
    
    for i in range(min_len):
        if sub[i] != ref[i]:
            return i
    if len(sub) != len(ref):
        return min_len
    
    return -1

print(diff("AATA", "AAAA"))
print(diff("CTTT","TTTT"))
print(diff("CCC", "CCCCC"))
print(diff("ACG", "ACG"))


def repair(sub, ref):
    first_mutation_index = diff(sub, ref)
    if first_mutation_index == -1:
        return sub
    
    best_repair = sub
    min_diff = len(ref)  # Initialize with maximum possible difference
    
    # Delete
    if first_mutation_index < len(sub):
        sub_delete = sub[:first_mutation_index] + sub[first_mutation_index + 1:]
        diff_delete = diff(sub_delete, ref)
        if diff_delete == -1 or diff_delete > first_mutation_index:
            best_repair = sub_delete
            min_diff = diff_delete

    # Substitute
    if first_mutation_index < len(sub) and first_mutation_index < len(ref):
        sub_substitute = sub[:first_mutation_index] + ref[first_mutation_index] + sub[first_mutation_index + 1:]
        diff_substitute = diff(sub_substitute, ref)
        if (diff_substitute == -1 or diff_substitute > first_mutation_index) and (diff_substitute == -1 or diff_substitute < min_diff):
            best_repair = sub_substitute
            min_diff = diff_substitute
        
    # Insert
    if first_mutation_index <= len(sub):  # Changed < to <= to allow insertion at the end
        sub_insert = sub[:first_mutation_index] + ref[first_mutation_index] + sub[first_mutation_index:]
        diff_insert = diff(sub_insert, ref)
        if (diff_insert == -1 or diff_insert > first_mutation_index) and (diff_insert == -1 or diff_insert < min_diff):
            best_repair = sub_insert
            min_diff = diff_insert
        
    return best_repair

# Test the function
print(repair("AATAGCA", "AAAGGA"))  # Expected output: "AAAGCA"
print(repair("ATAGG", "AAGG"))      # Expected output: "AAGG"
print(repair("ATA", "ATA"))          # Expected output: "ATA"
       
def count(sub, ref):
    """Counts the number of repairs needed to make sub equal to ref.
    
    Parameters:
    sub, ref: str, DNA genetic codes
    
    Returns:
    int: Number of changes needed to make sub equal to ref
    """
    count = 0
    while sub != ref:
        new_sub = repair(sub, ref)
        if new_sub == sub:
            # we need to count the remaining differences
            return count + diff(sub, ref)
        sub = new_sub
        count += 1
    
    return count

print(count("ACAAAGTAGTC", "AAAAAGTAGTA"))

if __name__ == "__main__": main()




s='AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
codon_table = {                                                 #This dictionary maps each possible three-nucleotide RNA codon to its corresponding amino acid
           "UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
           "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
           "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
           "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
           "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
           "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
           "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
           "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
           "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
           "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
           "UAA": "Stop", "CAA": "Q", "AAA": "K", "GAA": "E",
           "UAG": "Stop", "CAG": "Q", "AAG": "K", "GAG": "E",
           "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
           "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
           "UGA": "Stop", "CGA": "R", "AGA": "R", "GGA": "G",
           "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"}

#defining the function
def string_encoded (s):
    protein=''

    for i in range(0, len(s), 3):                       #for loop that iterates over the RNA sequence in steps of 3
        codon = s[i:i+3]                                #extracts the current three-nucleotide segment from the sequence.
        aminoacid = codon_table.get(codon, '')          #get  the corresponding amino acid from the codon_table. If the codon is not found, it returns an empty string.
        if aminoacid == 'Stop':
            break 
        protein += aminoacid                            #If the amino acid is valid (not "Stop"), it is appended to the protein string.
    return protein

s = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
protein= string_encoded (s)
print(protein)

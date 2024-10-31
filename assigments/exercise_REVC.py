
#defining the function
def reverse_complement(dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}    #dictionary that that associated each nucleotide to its complement
    
    dna_inversed = ""   
    
    #for loop that iterates over each nucleotide in the reversed version of dna.
    for i in reversed(dna):                
        dna_inversed += complement[i]      # for each nucleotide in the reversed string, adds the complement to dna_inversed
    
    return dna_inversed



dna_string = "AAAACCCGGT"
print(reverse_complement(dna_string))

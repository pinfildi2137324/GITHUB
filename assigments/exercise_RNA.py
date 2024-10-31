#defining the function
def transcribe_dna_to_rna(dna_string):                                          
    if not dna_string:                   #this checks if dna_string is empty. If it is, the function returns an empty string. Useful for stopping the transcription when there are no more nucleotides
        return ""                                                               
    else:
        first_nucleotide = 'U' if dna_string[0] == 'T' else dna_string[0]      #checking if the first nucleotide is equal to T. If yes, it is replaced with U, otherwise it remains T  
        return first_nucleotide + transcribe_dna_to_rna(dna_string[1:])        #call the first nucleotide and call the function again (using a DNA string without the first nucleotide), and concatenates them 

dna_string = "GATGGAACTTGACTACGTAAATT"
rna_string = transcribe_dna_to_rna(dna_string)    #calls the transcribe_dna_to_rna function with the dna_string as argument 

print(rna_string) 


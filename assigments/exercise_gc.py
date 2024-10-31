#This function calculates the GC content percentage of a given DNA string.
def calculate_gc_content(dna):                                   
    gc_count = dna.count('G') + dna.count('C')                    
    return (gc_count / len(dna)) * 100                           

# This function parses a FASTA formatted string into a dictionary.
def parse_fasta(fasta_str):                                      
    fasta_dict = {}                                              
    lines = fasta_str.strip().split('\n')                        
    seq_id = ""
    sequence = ""        

    for line in lines:                             
        if line.startswith('>'):                    
            if seq_id:  
                fasta_dict[seq_id] = sequence       
            seq_id = line[1:].strip()               
            sequence = ""                           
        else:
            sequence += line.strip()                

    if seq_id:                                
        fasta_dict[seq_id] = sequence         

    return fasta_dict                        

#This function finds the sequence with the highest GC content.
def find_highest_gc_content(fasta_str):        
    fasta_dict = parse_fasta(fasta_str)        
    max_gc_id = None
    max_gc_content = 0.0

    for seq_id, dna in fasta_dict.items():         
        gc_content = calculate_gc_content(dna)        
        if gc_content > max_gc_content:               
            max_gc_content = gc_content
            max_gc_id = seq_id                      
    return max_gc_id, max_gc_content


if __name__ == "__main__":
    fasta_input = """>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
"""
    
    seq_id, gc_content = find_highest_gc_content(fasta_input)
    print(f"{seq_id}\n{gc_content:.6f}")

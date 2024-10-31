#Counter Initialization
a=0
c=0
g=0
t=0

dna = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

# for loop that iterates over each nucleotide in the string dna
for n in dna:
    if n == 'A':
        a +=1
    elif n == 'C':
        c +=1
    elif n == "G":
        g+=1
    elif n == 'T':
        t +=1
print(a,c,g,t)
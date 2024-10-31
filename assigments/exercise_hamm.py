#defining the function
def hamming(s,t):
    if len(s) != len(t):
        raise ValueError             #if the lengths of the two strings are not equal the Hamming distance cannot be calculated 
    hamming_distance=0
    for i in range(len(s)):  
        if s[i] != t[i]:
            hamming_distance += 1
    return hamming_distance

s='GAGCCTACTAACGGGAT'
t='CATCGTAATGACGGCCT'
print(hamming(s,t))
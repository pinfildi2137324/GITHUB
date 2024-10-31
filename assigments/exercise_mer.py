#defining the function
def sorting (A,B):
    n=len(A)
    m=len(B)
    i=0
    j=0
    C=[]

    while i<n and j<m:                    #This while loop continues as long as there are elements in both A and B.
        if A[i] < B[j]:
            C.append(A[i])
            i+=1
        else:
            C.append(B[j])
            j+=1
    while i<n:                            #This loop handles any remaining elements in A after all elements in B have been added to C.
        C.append(A[i])
        i+=1
    while j<m:                            # this handles any remaining elements in B.
        C.append(B[j])
        j+=1

    return C

n=4
m=3
A='2 4 10 18'
B='-5 11 12'

array_A= A.split()
array_B= B.split()

A=[int(num) for num in array_A]
B=[int(num) for num in array_B]
C=sorting(A,B)
print(*C)


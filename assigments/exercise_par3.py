#defining the function
def permutation(n, A):
    n = len(A)
    if n == 0:
        return []
    x = A[0]                         # The pivot element
    less = []
    equal = []
    greater = []
    for i in range(n):               #This loop iterates through all elements of A.
        if A[i] < x:
            less.append(A[i])
        elif A[i] == x:
            equal.append(A[i])
        else:
            greater.append(A[i])

    B = less + equal + greater
    
    return B

n = 9
A = [4, 5, 6, 4, 1, 2, 5, 7, 4]
x1=0
B = permutation(n, A)
numbver=0

for x in B:
    print(B[numbver], end=',')
    numbver +=1
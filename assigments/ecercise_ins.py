#defining the function
def count_swaps(A):
    number_swap = 0
    n=len(A)

    for i in range(1, n):
        key = A[i]                      #key is the current element
        j = i - 1                       #j is initialized to the index of the previous element.
        
        while j >= 0 and A[j] > key:    #This loop shifts elements that are greater than key one position to the right, to make space for key.
            A[j + 1] = A[j]
            j -= 1                      #j is decremented to check the next element.
            number_swap += 1
        
            A[j + 1] = key              #After finding the correct position, key is placed in its correct position.
    return number_swap
        
n = 6
A = [6, 10, 4, 5, 1, 2]
swap = count_swaps(A)
print(swap)
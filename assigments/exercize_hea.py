def heapify(A, n, i):
    largest = i                # Initialize largest as root
    left = 2 * i + 1           
    right = 2 * i + 2  

    if left < n and A[left] > A[largest]:            # check if left child of root exists and is greater than root
        largest = left

    if right < n and A[right] > A[largest]:          # check if right child of root exists and is greater than root
        largest = right

    if largest != i:                                 # Change root, if needed
        A[i], A[largest] = A[largest], A[i]  # swap

        heapify(A, n, largest)

def build_max_heap(A):
    n = len(A)
    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(A, n, i)

n = 5
A = [1, 3, 5, 7, 2]
build_max_heap(A)

numbver=0
for x in A:
    print(A[numbver], end=' ')
    numbver +=1
    

def heapify(arr, n, i):
    largest = i                        # Initialize largest as root
    left = 2 * i + 1                   # left child index
    right = 2 * i + 2                  # right child index

    if left < n and arr[left] > arr[largest]:                # Check if left child exists and is greater than root
        largest = left

    if right < n and arr[right] > arr[largest]:              # Check if right child exists and is greater than largest so far
        largest = right

    if largest != i:                                          # If largest is not root, swap and continue heapifying
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements from heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Move current root to end
        heapify(arr, i, 0)

n = 9
A = [2, 6, 7, 1, 3, 5, 4, 8, 9]

heap_sort(A)

numbver=0
for x in A:
    print(A[numbver], end=' ')
    numbver +=1

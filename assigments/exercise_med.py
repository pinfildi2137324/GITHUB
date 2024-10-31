# This function rearranges the array such that all elements less than the pivot are on the left, and all elements greater are on the right.
def partition(A, left, right):
    pivot_value = A[right]                                # sets pivot_value as the last element.
    store_index = left                                    #is the starting index of the current segment of the array being processed.

    for i in range(left, right):
        if A[i] < pivot_value:
            A[store_index], A[i] = A[i], A[store_index]   #this line performs a swap
            store_index += 1                              #After the swap, store_index is incremented by 1

    # Move the pivot to its final place
    A[store_index], A[right] = A[right], A[store_index]
    return store_index

#This function implements the Quickselect algorithm.
def quickselect(A, left, right, k):
    if left == right:  
        return A[left]

    pivot_index = partition(A, left, right)

    if k == pivot_index:
        return A[k]
    elif k < pivot_index:
        return quickselect(A, left, pivot_index - 1, k)
    else:
        return quickselect(A, pivot_index + 1, right, k)

def find_kth_smallest(n, A, k):
    # Convert k to 0-indexed
    k -= 1
    return quickselect(A, 0, n - 1, k)


n = 11
A = [2, 36, 5, 21, 8, 13, 11, 20, 5, 4, 1]
k = 8
result = find_kth_smallest(n, A, k)
print(result)
    
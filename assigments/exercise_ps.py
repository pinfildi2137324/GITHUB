import heapq                          #This line imports the heapq module, which contains functions to work with heaps.

#defining the function
def k_smallest_elements(arr, k):
    min_heap = []                     #initialize an empty list to act as the min-heap.
    
    for num in arr:                          #The code iterates over each number in the array arr.
        heapq.heappush(min_heap, num)        #function adds each number to the min_heap.
    
    smallest_elements = []
    for i in range(k):                                        
        smallest_elements.append(heapq.heappop(min_heap))     #heapq.heappop(min_heap) This function removes and returns the smallest element from the min-heap min_heap.
    
    return smallest_elements


n = 10
A = [4, -6, 7, 8, -9, 100, 12, 13, 56, 17]
k = 3

result = k_smallest_elements(A, k)
number = 0
for x in result:
    print(result[number], end=' ')
    number += 1

#defining the function
def sort_array(n, A):
    A.sort()  # Sorts the array in place
    return A

# Sample input
n = 7
A = [5, -2, 4, 7, 8, -10, 11]
# Sorting the array
sorted_array = sort_array(n, A)

numbver=0
for x in sorted_array:
    print(sorted_array[numbver], end=' ')
    numbver +=1

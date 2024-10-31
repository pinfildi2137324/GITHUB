#defining the function
def partition(array):
    new_array, left_array, right_array = [], [], []
    new_array.append(array[0])                             #The first element of the input array is added to new_array as the pivot
    for i in range(1, len(array)):                         #This loop iterates over the elements in array starting from index 1
        if array[i] <= array[0]:                           #Each element is compared to the pivot 
            left_array.append(array[i])                    #If it's less than or equal to the pivot, it is added to left_array.
        else:
            right_array.append(array[i])                   #Otherwise, it goes into right_array
    new_array = left_array + new_array + right_array
    return new_array


n = 9  
A = [7, 2, 5, 6, 1, 3, 9, 4, 8]  

B = partition(A)
numbver=0
for x in B:
    print(B[numbver], end=' ')
    numbver +=1


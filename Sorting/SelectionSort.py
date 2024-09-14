def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

#Example
array = [4,5,2,1,-3,4,10,-12]
sorted_array = selection_sort(array)

#Printing the output 
print(f'Sorted Array is : {sorted_array}')
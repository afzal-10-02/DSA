def InsertionSort(arr):
    
    for i in range(1,len(arr)):
        key = arr[i]

        for j in reversed(range(i)):
            if key < arr[j]:
                arr[j+1] = arr[j]
            else:
                arr[j] =key
                break
    return arr

#Example 
array = [3,4,2,1,9,0,-2,-1]
sorted_array = InsertionSort(array)

#Print the Sorted Array
print(f'Sorted Array is : {sorted_array}')
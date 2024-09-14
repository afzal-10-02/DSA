def QuickSort(arr):

    if len(arr)<=1:
        return arr
    
    pivot = arr[-1]
    
    left = [x for x in arr if x<pivot]
    right = [x for x in arr if x>pivot]
    middle = [x for x in arr if x == pivot]

    return QuickSort(left) + middle + QuickSort(right)

#Example
array = [2,4,1,2,7,8,9,6,5,4,3,3,1,-3,-6]
sorted_array = QuickSort(array)

#Print the sorted Array
print(f'Sorted Array is : {sorted_array}')
def BubbleSort(arr):
    l = len(arr)

    for i in range(l):
        for j in range(l-i-1):
            if arr[j]>arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
    return arr

#Example 
array = [1,2,1,5,6,7,4,3,2,1]
sorted_array = BubbleSort(array)

#Print the Sorted array
print(f'Sorted Array is : {sorted_array}')
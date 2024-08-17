def BubbleSort(arr):
    l = len(arr)

    for i in range(l):
        for j in range(l-i-1):
            if arr[j]>arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
    return arr

print(BubbleSort([1,2,1,5,6,7,4,3,2,1]))
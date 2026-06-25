def sum( n):
    if(n ==1 ):
        return 1
    
    return n + sum(n-1)

# print(sum(5))

def mergeSort(arr):
    if(len(arr) <= 1):
        return
    mid = len(arr)// 2
    left = arr[:mid]
    right = arr[mid:]
    mergeSort(left)
    mergeSort(right)

    return merge(arr, left, right)


def merge(arr, left, right):
    i = j = k = 0
    merged = []

    # Merge left and right subarrays into merged
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Copy remaining elements from left subarray, if any
    while i < len(left):
        merged.append(left[i])
        i += 1

    # Copy remaining elements from right subarray, if any
    while j < len(right):
        merged.append(right[j])
        j += 1

    # Copy merged array back to arr
    for idx in range(len(merged)):
        arr[idx] = merged[idx]

    return arr






    
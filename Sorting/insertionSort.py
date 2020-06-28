def insertion(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

print('Enter the numbers seperated by space: ',end = '')
arr = [int(x) for x in input().split()]
insertion(arr)
print('Sorted array:',*arr)

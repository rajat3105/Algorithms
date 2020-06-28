def selection(arr):
    for i in range(len(arr)-1):
        min = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min]:
                min = j
        if min != i:
            arr[i],arr[min] = arr[min],arr[i]
        print(arr)

print('Enter the numbers seperated by space: ',end = '')
arr = [int(x) for x in input().split()]
selection(arr)
print('Sorted array:',*arr)

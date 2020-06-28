def binary(arr,x,start,end):
    if start<=end:
        mid = (start + end) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return binary(arr,x,mid+1,end)
        else:
            return binary(arr,x,start,mid-1)
    else:
        return -1

print('Enter the numbers seperated by space: ',end = '')
arr = [int(i) for i in input().split()]
x = int(input('Enter the number you want to find in array: '))
result = binary(arr,x,0,len(arr)-1)
if result == -1:
    print('Not found :(')
else:
    print('The number is at index',result)

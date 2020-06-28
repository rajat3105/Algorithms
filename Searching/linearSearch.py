def linear(arr,x):
    n = len(arr)
    for i in range(n):
        if arr[i] == x:
            return i
    return -1

print('Enter the numbers seperated by space: ',end = '')
arr = [int(i) for i in input().split()]
x = int(input('Enter the number you want to find in array: '))
result = linear(arr,x)
if result == -1:
    print('Not found :(')
else:
    print('The number is at index',result)

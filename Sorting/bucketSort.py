def insertion(arr1):
    for i in range(1,len(arr1)):
        key = arr1[i]
        j = i - 1
        while j >= 0 and key < arr1[j]:
            arr1[j+1] = arr1[j]
            j -=1
        arr1[j+1] = key
    return arr1

def bucket(arr):
    temp = []
    slot = 10
    for i in range(slot):
        temp.append([])
    for j in arr:
        ind = int(slot * j)
        temp[ind].append(j)
    for i in range(slot):
        temp[i] = insertion(temp[i])
    k = 0
    for i in range(slot):
        for j in range(len(temp[i])):
            arr[k] = temp[i][j]
            k += 1
    return arr

print('Enter the numbers seperated by space: ',end = '')
arr = [float(x) for x in input().split()]
bucket(arr)
print('Sorted array:',*arr)

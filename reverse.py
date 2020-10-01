def reverse(arr,start,end):
             while(start<end):
                 arr[start],arr[end]=arr[end],arr[start]
                 start=start+1
                 end=end-1
                
def left(arr,position):
    if position==0:
        return
    reverse(arr,0,position-1)
    reverse(arr,position,n-1)
    reverse(arr,0,n-1)
    
n=int(input("Enter number of elements in array: "))
list=[None]*n
for i in range(n):
    list[i]=int(input())
position=int(input("Enter position: "))

    
left(list,position)
print(list)
    

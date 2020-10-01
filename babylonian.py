def root(n):
    x=n
    y=1
    
    e=0.001          # e difines the accuracy level
    while(x-y>e):
        x=(x+y)/2
        y=n/x
        
    return x
n= int(input("Enter the number whose square root you need to found : "))
print("Root is: ", round(root(n),3))

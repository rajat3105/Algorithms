def fac(n):
    if n==0:
        return 1
    else:
        return n*fac(n-1)
    
def strongnum(num):
    out=[]
    sum=0
    while(num>0):
        p=num%10
        sum=sum+fac(p)
        num=num//10
    return sum
        
num=int(input("enter number to check for strong number: "))
strong=strongnum(num)

if(num==strong):
    print("Yes!! it is a strong number ")
    
else:
    print("Not a strong number ")
        
    

n=int(input())
a=0
b=1
count=0
if n<1:
    print("enter positive number")
elif n==1:
    print(a)
else:
    while count<n:
        print(a)
        c=a+b
        a=b
        b=c
        count=count+1
        

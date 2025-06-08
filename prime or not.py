a=int(input())
if a==1:
    print("prime")
elif a>1:
    for i in range(2,a):
        if a%i==0:
            print("not prime")
        else:
            print("prime")
            break
else:
    print("not prime")

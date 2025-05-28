def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
n1=int(input())
if fact(n1)==n1:
    print("strong")
else:
    print("not")

r=int(input())

for i in range(r):
    n=1
    for j in range(r-i-1):
        print(" ",end=" ")
    for k in range(i +1):
        print(n,end="   ")
        n=n*(i-k)//(k+1)
    print()

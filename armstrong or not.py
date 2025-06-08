a=input()
b=int(a)
l=len(a)
count=0
for i in a:
    c=int(i)**l
    count=count+c
d=count
if(d==b):
    print("armstrong")
else:
    print("not")
    

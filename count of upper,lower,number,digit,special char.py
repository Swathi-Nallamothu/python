def count(a):
    print((sum(1 for i in a if i.isupper())))  
    print((sum(1 for i in a if i.islower())))  
    print((sum(1 for i in a if i.isdigit()))) 
    print((sum(1 for i in a if not i.isalnum()))) 
a=input()
count(a)

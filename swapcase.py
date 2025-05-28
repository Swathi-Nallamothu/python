a=input()
print(a.encode())
print(a.swapcase())#or casefold #upper-lower,lower-upper
print(a.upper())#to upper
print(a.lower())#to lower
print(a.title())#each word first letter will upper
print(a.capitalize())#first letter of sentence will upper
b=a.split(" ")
for i in b:
    print(i.capitalize(),end=" ")#each word first letter will upper

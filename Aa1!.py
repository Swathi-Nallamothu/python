a= "tfgvhbwnESDTFCHGVB2138749#$%^&^&*("
upper="".join([char for char in a if char.isupper()])
lower="".join([char for char in a if char.islower()])
num="".join([char for char in a if char.isdigit()])
special_chars ="".join([char for char in a if not char.isalnum()])
result= upper+lower+ num+special_chars
print(result)


#https://github.com/Swathi-Nallamothu/calculator/commit/7213f68a37725ea060e997e38f8bddc5c62809ec
import math
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y
def square_root(x):
    return math.sqrt(x)
def power(x, y):
    return math.pow(x, y)
def logarithm(x, base):
    return math.log(x, base)
def sine(x):
    return math.sin(math.radians(x))
def cosine(x):
    return math.cos(math.radians(x))
def tangent(x):
    return math.tan(math.radians(x))

print("Select operation:")
print("1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Square Root\n6.Power\n7.Logarithm\n8.Sine\n9.Cosine\n10.Tangent")

choice = input("Enter choice (1-10): ")

if choice in ['1', '2', '3', '4', '6']:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    operations = {'1': add, '2': subtract, '3': multiply, '4': divide, '6': power}
    print(f"Result: {operations[choice](num1, num2)}")

elif choice == '5':
    num = float(input("Enter number: "))
    print(f"Result: {square_root(num)}")

elif choice == '7':
    num = float(input("Enter number: "))
    base = float(input("Enter base: "))
    print(f"Result: {logarithm(num, base)}")

elif choice in ['8', '9', '10']:
    num = float(input("Enter angle in degrees: "))
    
    trig_operations = {'8': sine, '9': cosine, '10': tangent}
    print(f"Result: {trig_operations[choice](num)}")

else:
    print("Invalid input")

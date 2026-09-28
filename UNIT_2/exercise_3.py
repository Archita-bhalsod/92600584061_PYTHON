'''Write a program to generate a multiplication table using a for loop'''

num = int(input("Enter the number: "))

print(f"Multiplication Table of {num}:")

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

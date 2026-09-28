'''write a program to find a sum of digit of a number using a while loop.'''
num = int(input("Enter a number: "))

total_sum = 0

while num > 0:
    digit = num % 10       
    total_sum += digit   
    num = num // 10 

print(f"Sum of digits: {total_sum}")

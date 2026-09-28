'''write a program to check whether a number is positive negative or zero using nested conditions.'''
num = int(input("Enter your number: "))
if num >= 0:
    if num == 0:
        print("Number is Zero.")
    else:
        print("Number is positive.")
else:
    print("Number is Negative.")

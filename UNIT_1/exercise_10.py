#Write a program to demonstrate recursion using factorial or Fibonacci series.
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = 5
print("Factorial =",factorial(num))

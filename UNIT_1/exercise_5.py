#write a program to create and manipulate lists using indexing  slicing and list comprehensions.

numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)
print("First item:", numbers[0])
print("Last item:", numbers[-1])

numbers[1] = 99
print("After changing index 1:", numbers)

numbers = [10, 20, 30, 40, 50]

print("Slice [1:4]:", numbers[1:4])
print("Reversed list:", numbers[::-1])

doubled = [x * 2 for x in numbers]
print("Doubled list:", doubled)

filtered = [x for x in numbers if x > 25]
print("Numbers > 25:", filtered)

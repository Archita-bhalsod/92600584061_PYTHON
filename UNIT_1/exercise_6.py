#write a program to illustrate the use of tuples and sets with basic operations.

my_tuple = ("apple", "banana", "apple")

print("First item:", my_tuple[0])
print("Count of apple:", my_tuple.count("apple"))


set_A = {1, 2, 3}
set_B = {3, 4, 5}

set_A.add(9)                  
print("Updated Set A:", set_A)

print("In both sets:", set_A.intersection(set_B))  

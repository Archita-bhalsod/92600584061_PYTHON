#write a python program to demonstrate string operations including slicing formatting and build in string function.
text = "Hello World"

print("First 5 characters:", text[:5])
print("Last 5 characters:", text[-5:])

name = "Alice"
age = 20
print(f"My name is {name} and I am {age} years old.")

print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Replace 'World' with 'Python':", text.replace("World", "Python"))
print("Length of text:", len(text))

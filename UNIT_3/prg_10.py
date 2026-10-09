
import re

with open("data.txt", "r") as f:
    text = f.read()

name = re.search(r"Name: (.+)", text)
age = re.search(r"Age: (\d+)", text)
phone = re.search(r"Phone: (\d+)", text)

print("Name =", name.group(1))
print("Age =", age.group(1))
print("Phone =", phone.group(1))

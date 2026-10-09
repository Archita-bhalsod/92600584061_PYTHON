
import re

text = "Python is easy. Python is useful."

print(re.match("Python", text))
print(re.search("easy", text))
print(re.findall("Python", text))


import os
import sys

print("Current directory =", os.getcwd())

os.mkdir("myfolder")
print("Directory created")

print("Python version =", sys.version)

print("Files =", os.listdir())

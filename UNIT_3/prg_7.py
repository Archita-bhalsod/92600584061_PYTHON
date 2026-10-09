
import shutil
import os

with open("a.txt", "w") as f:
    f.write("Hello Python")

shutil.copy("a.txt", "b.txt")
print("File copied")

shutil.move("b.txt", "myfile.txt")
print("File moved")

os.remove("myfile.txt")
print("File deleted")

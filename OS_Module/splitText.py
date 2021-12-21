import os

path = str(input("Enter your path: "))

array = os.path.splitext(path)

print("This is the file name: " + array[0])
print("This is the extension: " + array[1])
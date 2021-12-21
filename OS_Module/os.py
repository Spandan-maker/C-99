import os

#date = os.system("date")
#print(date)

# Makes folder in the same folder
#os.mkdir("OS_Folder")

# Makes folder outside this folder
#os.mkdir("../OS_Folder")

# Makes folder at the 2nd level
#os.mkdir("../../OS_Folder")

thisCWD = os.getcwd()
print(thisCWD)

dir = os.listdir()
print(dir)
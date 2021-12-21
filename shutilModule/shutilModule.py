import os
import shutil

source = "shutilModule.py"
destination = "Shutil_Module"

#data = shutil.copy(source, destination)

data = shutil.move(source, destination)
print(os.listdir("OS_Module"))
import os
from posixpath import splitext
import shutil
path=input('enter the path: ')

list_of_directories=os.listdir(path)

for file in list_of_directories:
    name,ext=os.path.splitext(file)
    ext=ext[1:]
    if ext == "":
        continue
    if os.path.exists(path+"/"+ext):
        shutil.move(path+"/"+file,path+"/"+ext+"/"+file)
    else:
        os.mkdir(path+"/"+ext)
        shutil.move(path+"/"+file,path+"/"+ext+"/"+file)